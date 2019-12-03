######################################
# @auther: Richard Li from USTC, China
######################################

from RBtree import *
from order_search_tree import *

class Interval_Node(OS_Node):
    def __init__(self, interval:tuple= (None,None), size = 0, color ='b', p=None, left=None, right=None):
        self.interval = interval
        self.value = interval[0]
        self.max = interval[1]
        
        self.size = size
        self.color = color
        self.p = p
        self.left = left
        self.right = right

    def print_node(self):
        print(f"{self.color}: {self.interval}, L: {self.left.interval} R:{self.right.interval}")

class Interval_Tree(OrderSearchTree):
    def __init__(self):
        ''' Initialize the red black tree: just create the T.nil node. '''
        self.nil_node = Interval_Node() # the color of nil_node is black
        self.root = self.nil_node # now self.node and self.nil_node are pointed to the same class instance
    
    def get_node_max(self,x,x1,x2):
        '''
            Get the max value from int x, x1, x2
            Note: x1, and x2 can be None!
        '''
        if x1== None:
            if x2== None:
                return x
            else:
                return max(x, x2)
        elif x2== None:
            return max(x, x1)
        else:
            return max(x, x1, x2)

    def rotate(self, mode, x):
        '''
            mode: left rotate & right rotate
            x: the node that to be rotated
            Note: need to update size after rotation!
        '''
        if mode == 'left':
            y = x.right
            # y.print_node() #FIXME
            x.right = y.left # let y.left tree be the right tree of x
            # y.left.print_node() #FIXME
            if y.left.value !=None:
                y.left.p = x # nil_node also has "parent" property!
            
            y.p = x.p
            if x.p.value == None: # x is the root 
                self.root = y
            elif x.p.left == x:
                x.p.left = y
            else:
                x.p.right = y
            
            y.left = x
            x.p = y

            # update size
            y.size = x.size
            x.size = x.left.size + x.right.size + 1 

        if mode == 'right':
            y = x.left
            # y.print_node() #FIXME
            x.left = y.right# let y.left tree be the right tree of x
            # y.left.print_node() #FIXME
            if y.right.value != None:
                y.right.p = x # nil_node also has "parent" property!
            
            y.p = x.p
            if x.p.value == None: # x is the root 
                self.root = y
            elif x.p.left == x:
                x.p.left = y
            else:
                x.p.right = y
            
            y.right = x
            x.p = y
            
            # update size
            x.size = y.size
            y.size = y.left.size + y.right.size + 1 
        
        # Finally, update max property
        x.max = self.get_node_max(x.interval[1], x.left.max, x.right.max)
        y.max = self.get_node_max(y.interval[1], y.left.max, y.right.max)

    def insert(self, node_interval):
        '''
            Insert node with node_value into the rbTree.
        '''
        z = Interval_Node(interval= node_interval,size= 1)
        y = self.nil_node
        x = self.root
        
        while x.value != None:  # x != self.nil_node -> should be x.value != None
            y = x # Use y to record position of x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
            y.size += 1
            y.max = self.get_node_max(y.max, None, z.max)

        z.p = y
        if y == self.nil_node: # When tree is empty!
            self.root = z
        elif z.value < y.value:
            y.left = z
        else :
            y.right = z

        z.left = self.nil_node
        z.right = self.nil_node
        z.color = 'r' # color is red 
        
        self.insert_fixup(z)

    def delete(self, z): 
        '''
            delete node z in rbTree, z need to be searched first.
        '''
        if z == None:
            print("[ERR] delete a None node.")
            return None
        # update size of z's parents and go upward
        temp = z
        while temp != self.root:
            temp = temp.p
            temp.size -=1
    
        y = z
        y_origin_color = z.color # save the color of z
        
        if z.left == self.nil_node:
            x = z.right
            x = self.transplant(z,z.right) 
            temp = x # update temp, in order to update max upwards later
            # Note: here no need to update x.size and x.max
        elif z.right == self.nil_node:
            x = z.left
            x = self.transplant(z,z.left)
            temp = x

        # if z has left and right children
        else:
            y = self.getmin(z.right)
            y_origin_color = y.color
            x = y.right
            if y.p == z:    # y is the right child of z
                x.p = y
            else:
                x.p = y.p   # y is not the right child of z
                y.p.left = x
                
                y.right = z.right
                y.right.p = y

            # shared by both conditions:
            y = self.transplant(z,y)
            y.left = z.left
            y.left.p = y
            y.color = z.color
            y.size = y.left.size + y.right.size + 1 # update y.size
            y.max = self.get_node_max(y.interval[1], y.left.max, y.right.max) # update y.max
            temp = y

        # update max upwards
        while temp != self.root:
            temp = temp.p
            temp.max = self.get_node_max(temp.interval[1], temp.left.max, temp.right.max)

        del z
        if y_origin_color == 'b':
            # 3 conditions
            # print(x.p.value) # FIXME
            self.delete_fixup(x)
        
    def search_fist_overlap_interval(self,interval:tuple):
        '''
            interval is a tuple 
        '''
        x = self.root
        while x != self.nil_node:
            # interval: [], x.interval:{}
            # overlap: interval[0] < x.interval[1] and interval[1] > x.interval[0]
            # 1. { [ ] } 
            # 2. { [ } ] 
            # 3. [ { ] }
            # 4. [ { } ]           
            if interval[0] < x.interval[1] and interval[1] > x.interval[0]:
                return x.interval
            # [] {}
            # Wrong: elif interval[1] <= x.interval[0] and x.left!=self.nil_node and x.left.max >= interval[0]:
            elif x.left !=self.nil_node and x.left.max >= interval[0]:
                x = x.left                
            # {} []
            elif x.right!= self.nil_node and x.right.max >= interval[0]:
                x = x.right
            else:
                return None

        return None # not found

    def draw_node(self,f,x):
        if x.value !=None:
            if x.color == 'r':
                f.write(f"\"{x.interval}|{x.size}|{x.max}\"[color = \"red\"]\n")
            else:
                f.write(f"\"{x.interval}|{x.size}|{x.max}\"\n")            
            
            if x.left.value != None:
                f.write(f"\"{x.interval}|{x.size}|{x.max}\" -> \"{x.left.interval}|{x.left.size}|{x.left.max}\"\n")
            if x.right.value != None:
                f.write(f"\"{x.interval}|{x.size}|{x.max}\" -> \"{x.right.interval}|{x.right.size}|{x.right.max}\"\n")
            self.draw_node(f,x.left)
            self.draw_node(f,x.right)

        
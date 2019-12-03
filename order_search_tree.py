from RBtree import *

class OS_Node(Node):
    def __init__(self, value=None, size = 0, color ='b', p=None, left=None, right=None):
        self.value = value
        self.color = color
        self.size = size
        self.p = p
        self.left = left
        self.right = right

class OrderSearchTree(RedBlackTree):
    def __init__(self):
        self.nil_node = OS_Node() # the color of nil_node is black
        self.root = self.nil_node

    def os_select(self, x, i):
        '''
            get the No.i min element in subtree with x as its root. 
            return: node
        '''
        rank = x.left.size + 1
        if i == rank:
            return x
        elif i < rank:
            return self.os_select(x.left, i)
        else:
            return self.os_select(x.right, i - rank)
    
    def os_getRank(self, x):
        '''
            get the rank of node x in osTree.
            return: int 
        '''
        rank = x.left.size + 1
        y = x
        while y != self.root: 
            if y == y.p.right:
                rank = y.p.left.size + 1 + rank
            y = y.p
        return rank

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

    def insert(self, node_value):
        '''
            Insert node with node_value into the rbTree.
        '''
        z = OS_Node(value= node_value, size= 1)
        y = self.nil_node
        x = self.root
        while x.value != None:  # x != self.nil_node -> should be x.value != None
            y = x # Use y to record position of x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
            y.size += 1 # update size along the path!
        z.p = y
        if y.value == None: # When tree is empty!
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
            # Note: here no need to update x.size
        elif z.right == self.nil_node:
            x = z.left
            x = self.transplant(z,z.left)

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
        del z
        if y_origin_color == 'b':
            # 3 conditions
            # print(x.p.value) # FIXME
            self.delete_fixup(x)
          
    def draw_node(self,f,x):
        if x.value !=None:
            if x.color == 'r':
                f.write(f"\"{x.value}|{x.size}\"[color = \"red\"]\n")
            else:
                f.write(f"\"{x.value}|{x.size}\"\n")            
            if x.left.value != None:
                f.write(f"\"{x.value}|{x.size}\" -> \"{x.left.value}|{x.left.size}\"\n")
            if x.right.value != None:
                f.write(f"\"{x.value}|{x.size}\" -> \"{x.right.value}|{x.right.size}\"\n")
            self.draw_node(f,x.left)
            self.draw_node(f,x.right)


             

    
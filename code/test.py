from RBtree import *
from order_search_tree import *
from Interval_tree import *
from copy import deepcopy
import numpy as np
import random

def final_os():
    T = OrderSearchTree()
    a = np.random.randint(1,100,80)
    print(a)
    T.insert_from_list(a)
    T.draw("osTree")

def final_interval():
    T = Interval_Tree()
    n = 20
    l = []
    for i in range(n):
        a = random.randint(0,100)
        b = random.randint(a,a+10)
        l.append((a,b))
    T.insert_from_list(l)
    T.draw("intervalTree")
    l.sort()
    print(l)
    # # print(l[n//4])
    # c = T.os_select(T.root, n//4 + 1)
    # print(c.interval)
    # T.delete(c)
    # T.draw("intervalTree")

    # # print(l[n//2])
    # c = T.os_select(T.root, n//2 + 1)
    # print(c.interval)
    # T.delete(c)
    # T.draw("intervalTree")



def os_2():
    T = OrderSearchTree()
    T.insert_from_list([0,5,6,8,15,16,17,25,19,26])
    T.draw("osTree")

def os_1():
    T = OrderSearchTree()
    T.insert_from_list([0,5,6,8,15,16,17,25,19,26])
    # T.insert_from_list([0,5,6,8,15])
    n = 10
    T.draw("osTree")
    a = T.os_select(T.root, 5)
    # print(a.value)
    T.delete(a)
    T.draw("osTree")
    b = T.os_select(T.root, 2)
    # print(b.value) 
    T.delete(b)
    T.draw("osTree")

def d():
    '''interval tree'''
    T = Interval_Tree()
    a = [(0,3),(5,8),(6,10),(8,9),(15,23),(16,21),(17,19),(25,30),(19,20),(26,26)]
    # a = [(0,3),(5,8),(6,10),(8,9),]
    T.insert_from_list(a)
    T.draw("interval_tree")
    # b = T.os_select(T.root, 8)
    b = T.search(25)
    T.delete(b)
    T.draw("interval_tree")
    c= T.search_fist_overlap_interval((27,28))
    print(c)

def c():
    T = RedBlackTree()
    a = [3, 12, 7, 10, 15, 16, 14, 17, 19, 20, 21, 23, 28, 30, 26, 41, 47, 33, 38, 39]
    # a = [0,5,6,8,15,16,17,25,19,26]
    # a.sort()
    # T.insert_from_list([3, 12, 7, 10, 15, 16, 14, 17, 19, 20, 21, 23, 28, 30, 26, 41, 47, 33, 38, 39])
    T.insert_from_list(a)
    T.insert_from_list([0,5,6,8,15,16,17,25,19,26])
    # T.insert_from_list([0,5,6,8,15,16,17,25,19,26])
    T.draw()


def a(T):
    z = T.search(8)
    T.delete(z)
    T.draw()

def b():
    x = Node(1)
    z = Node(0)
    m = Node(2)
    x.p = m
    # y = deepcopy(x)
    y = x 
    y.p = z
    y.color = 'r'
    print(x.color,y.color) # b r 
    print(x.p.value,y.p.value) # b r 

if __name__ == "__main__":
    # T = RedBlackTree()
    # T.insert_from_list([0,5,6,8,15,16,17,25,19,26])
    # T.draw()
    # a(T)

    # os_1()

    # os_2()
    
    # d()

    # final_os()
    final_interval()
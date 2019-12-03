# RedBlackTree, and more!
Hi there! Here is my code with detailed comments for red-black Tree, order search tree and interval tree, and I wrote them when I was learning the textbook "Introduction to Algorithms".

## Dependency
1. python >= 3.6
2. graphviz: if you want to draw the tree, you need it.
3. (choose) numpy: in ``test.py`` I used ``numpy.random.randint``, but of course you can just use module ``random`` instead.

## What I implemented
1. Read-black tree in [``RBtree.py``](./code/RBtree.py)
    + insert
    + delete
    + search
    + draw 

2. Order search tree in [``order_search_tree.py``](./code/order_search_tree.py)
    + insert
    + delete
    + search
    + draw 
    + select the i-least element

3. Interval tree in [``Interval_tree.py``](./code/Interval_tree.py)
    + insert
    + delete
    + search
    + draw 
    + select the i-least element
    + search first overlap interval

The relationship of inheritance is: Interval tree -> Order search tree -> Read-black tree

## How to draw the tree
![](./imgs/tree2.png)

Here is the image of a interval tree drawn using graphviz. 

For example, the meaning of ``(8,9)|9|26`` is ``interval|size|max``

+ size: the number of node in the subtree with the current node as its root.
+ max: the max interval.high in the subtree with the current node as its root.

(If you have no idea what these properties mean, please go and check out textbook "Introduction to Algorithms".)

The image above is drawn using graphviz and the information of this image is saved in ``interval_tree.gv``. 

Here is another more complicated order search tree. the ``44|63`` in root node means ``value|size``

![](./imgs/osTree.png)

## Lisence
This repository is of MIT lisence.

Author is Richard Li from USTC, China.

## Last but not least
If you find any bug, feel free to fix it and create pull request.

If you like it, click on the "star"! Thx.

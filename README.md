# RedBlackTree, and more!
Hi there! Here is my code with detailed comments for red-black Tree, order search tree and interval tree, and I wrote them when I was learning the textbook "Introduction to Algorithms".

## Dependency
1. python >= 3.6
2. graphviz: if you want to draw the tree, you need it.
3. (choose) numpy: in ``test.py`` I used ``numpy.random.randint``, but of course you can just use module ``random`` instead.

## What I implemented
1. Read-black tree in ``RBtree.py``
2. Order search tree in ``order_search_tree.py``
3. Interval_tree in ``Interval_tree.py``

## How to draw the tree
![](./imgs/tree2.png)

Here is the image of a interval tree drawn using graphviz. 

For example, the meaning of ``(8,9)|9|26`` is ``interval|size|max``

+ size: the number of node in the subtree with the current node as its root.
+ max: the max interval.high in the subtree with the current node as its root.

(If you have no idea what this properties mean, check out textbook "Introduction to Algorithms")

This image is drawn using graphviz. The information of this image is saved in ``interval_tree.gv``. 

Here is another more complicated order search tree. the ``44|63`` in root node means ``value|size``

![](./imgs/osTree.png)

## Lisence
This repository is of MIT lisence.

Author is Richard Li from USTC, China.

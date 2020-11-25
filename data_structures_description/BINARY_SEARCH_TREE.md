## Binary Tree (BT)
In this tree each node has max 2 childs and for [Binary Search Tree](https://github.com/kotsky/py-libs/blob/master/data_structures/bst.py) following condition is applied `node.left.value < node.value <= node.right.value`.
```
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
		
class Tree:
    def __init__(self, value):
		self.root = Node(value)
```
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/bst_vs_not_bst.png)
Besides that, Balanced Binary Tree has log(N) depth, and not-balanced tree might reach full N depth.
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/complete_binary_tree.png)
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/full_binary_tree.png)
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/perfect_binary_tree.png)

### BST Algorithms / Problems
There are the follows:
	- [Traversal methods](https://github.com/kotsky/py-libs/blob/master/algorithms/binary_tree_traversal.py)
	- BST validation
	- Find out the min depth from a sorted array
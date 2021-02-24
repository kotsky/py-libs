"""AVL Tree

#### Complexity
Insertion	Deletion	Search
O(log n)	O(log n)	O(log n)

Methods:
    insert
    delete
    search
    preorder traverse

Example:

if __name__ == '__main__':
    # nums = [1, 2, 3, 100, 4]
    # nums2 = [2, 3, 100]
    #
    # myTree = AVLTree()
    # root = None
    # for num in nums:
    #     myTree.insert(num)
    # print(myTree)
    #
    # for num in nums2:
    #     myTree.delete(num)
    # print("After Deletion: ")
    # print(myTree)

    myTree = AVLTree()

    while True:
        user_input = input()
        commands = user_input.split(' ')
        if commands[0] == "insert":
            myTree.insert(int(commands[1]))
        elif commands[0] == "delete":
            myTree.delete(int(commands[1]))
        elif commands[0] == "search":
            if myTree.search(int(commands[1])):
                print("That key is in the tree")
            else:
                print("There is no such key in the tree")
        elif commands[0] == "preorder":
            myTree.traverse()
        print(myTree)


"""

import sys


class AVLNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __repr__(self):
        self.printHelper(self.root, "", True)
        return ""

    def insert(self, key):
        # self.size += 1
        if self.root is not None:
            self.insert_node(self.root, key)
        else:
            self.root = AVLNode(key)

    # Function to insert a node
    def insert_node(self, node, key):

        # Find the correct location and insert the node
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self.insert_node(node.left, key)
        else:
            node.right = self.insert_node(node.right, key)

        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        # Update the balance factor and balance the tree
        balance_factor = self.getBalance(node)
        if balance_factor > 1:
            if key < node.left.key:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)

        if balance_factor < -1:
            if key > node.right.key:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)

        return node

    def delete(self, key):
        if key == self.root.key:
            self.root = self.delete_node(self.root, key)
        else:
            self.delete_node(self.root, key)

    # Function to delete a node
    def delete_node(self, node, key):

        # Find the node to be deleted and remove it
        if not node:
            return node
        elif key < node.key:
            node.left = self.delete_node(node.left, key)
        elif key > node.key:
            node.right = self.delete_node(node.right, key)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self.getMinValueNode(node.right)
            node.key = temp.key
            node.right = self.delete_node(node.right,
                                          temp.key)
        if node is None:
            return node

        # Update the balance factor of nodes
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        balanceFactor = self.getBalance(node)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(node.left) >= 0:
                return self.rightRotate(node)
            else:
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        if balanceFactor < -1:
            if self.getBalance(node.right) <= 0:
                return self.leftRotate(node)
            else:
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        return node

    # Function to perform left rotation
    def leftRotate(self, z):
        is_root = self.root == z
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        if is_root:
            self.root = y
        return y

    # Function to perform right rotation
    def rightRotate(self, z):
        is_root = self.root == z
        y = z.left
        z.left = y.right
        y.right = z
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        if is_root:
            self.root = y
        return y

    # Get the height of the node
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    # Get balance factor of the node
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def getMinValueNode(self, node):
        if node is None or node.left is None:
            return node
        return self.getMinValueNode(node.left)

    def traverse(self):
        self.preOrder(self.root)
        print('', end='\n')

    def preOrder(self, node):
        if not node:
            return
        print("{0} ".format(node.key), end="")
        self.preOrder(node.left)
        self.preOrder(node.right)

    def search(self, key):
        return self.searchHelper(self.root, key)

    def searchHelper(self, node, key):
        while node is not None:
            if key == node.key:
                return True
            elif node.key < key:
                node = node.right
            else:
                node = node.left
        return False

    # Print the tree
    def printHelper(self, curr_ptr, indent, last):
        if curr_ptr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr_ptr.key)
            self.printHelper(curr_ptr.left, indent, False)
            self.printHelper(curr_ptr.right, indent, True)

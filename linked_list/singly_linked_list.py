"""
In this file Singly Linked List (SLL) is presented with the following methods:
    1. Create: ll = SinglyLinkedList() -> creates head, tail of SLL
    2. To add node by its value to the end of LL: ll.addNode(value) -> will update tail
    3. To generate random SLL with user's size: ll.generateRandomSinglyLinkedList(size)
    4. To print SLL: ll.printLinkedList()
    5. To sort SLL without memory usage: ll.sortBubble()   # O(N^2) worst Time / O(1) Space
    6. Merge Sort Algorithm: ll.sortMerge()  # O(N*log(N)) Time / O(log(N)) Space

Example:
    ll = SinglyLinkedList()
    ll.generateRandomSinglyLinkedList(10)
    ll.printLinkedList()
    ll.sortBubble()
    ll.printLinkedList()
    
    kk = SinglyLinkedList()
    kk.generateRandomSinglyLinkedList(10)
    kk.printLinkedList()
    kk.sortMerge()
    kk.printLinkedList()
"""


class SinglyLinkedList:
    class LinkedListNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.is_sorted = False

    def generateRandomSinglyLinkedList(self, size):
        import random
        for i in range(size):
            val = random.random()
            val = int(val * 10)
            self.addNode(val)
        self.is_sorted = False

    def addNode(self, value):
        node = self.LinkedListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.is_sorted = False

    def removeInLine(self, prev_node, node):
        prev_node.next = node.next
        node = None
        return prev_node.next

    def printLinkedList(self):
        if self.head is None:
            print("There is not Linked List to sort. Please, add nodes")
            return
        node = self.head
        print("None", end="->")
        while node is not None:
            print(node.value, end="->")
            node = node.next
        print("None")

    def swapInPlace(self, node_one, node_two):
        temp = node_two.value
        node_two.value = node_one.value
        node_one.value = temp
        temp = None
        self.is_sorted = False

    # Bubble algorithms: Time O(N^2) worst / Space O(1)
    def sortBubble(self):
        if self.head is None:
            print("There is not Linked List to sort. Please, add nodes")
            return
        if self.is_sorted:
            # print("This Singly Linked List is sorted")
            return
        is_sorted = False
        while is_sorted is False:
            is_sorted = True
            node = self.head
            while node.next is not None:
                if node.value > node.next.value:
                    self.swapInPlace(node, node.next)
                    is_sorted = False
                node = node.next
        self.is_sorted = True

    def sortMerge(self):
        if self.is_sorted:
            print("There is not Linked List to sort. Please, add nodes")
            return
        self.is_sorted = True
        return self.sortMergeHelper(self.head)

    def sortMergeHelper(self, head_one):
        if head_one is None or head_one.next is None:
            return head_one

        middle_node = self.getMiddle(head_one)
        head_two = middle_node.next
        middle_node.next = None

        head_one = self.sortMergeHelper(head_one)
        head_two = self.sortMergeHelper(head_two)

        self.head = self.mergeSortedSinglyLinkedLists(head_one, head_two)

        return self.head

    def mergeSortedSinglyLinkedLists(self, head_one, head_two):
        if head_one is None or head_two is None:
            return head_two if head_two is not None else head_one

        p1 = head_one
        p1_prev = None
        p2 = head_two
        while p1 is not None and p2 is not None:
            if p1.value < p2.value:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev is not None:
                    p1_prev.next = p2
                p1_prev = p2
                p2 = p2.next
                p1_prev.next = p1
        if p1 is None:
            p1_prev.next = p2
        return head_one if head_one.value < head_two.value else head_two

    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and \
                fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

"""
Doubly Linked List (DLL) implementation.
bindNodes(nodeOne, nodeTwo) as an addition assest for node's reassigning.

DLL methods:
	1. Create entity dll = DoublyLinkedList;
	2. dll.setHead(node)  # set new "head" with new "node"; Time O(1)
	3. dll.setTail(node)  # similar to setHead
	4. dll.insertBefore(node, nodeToInsert)  # to insert new node before "node"
	5. dll.insertAfter(node, nodeToInsert)  # to insert new node after "node"
	6. dll.insertAtPosition(numberOfPosition, nodeToInsert)	 # insert "node" in
	certain place.
	7. dll.removeNodesWithValue(value)  # remove node in LL with that "value"
	8. dll.remove(node)  # remove that "node"
	9. dll.containsNodeWithValue(value)  # to find out if LL has "node" with that "value"
	10. dll.printLinkedList()  # print DLL out in console
	
Example:
	linkedList = DoublyLinkedList()
	one = Node(1)
	two = Node(2)
	three = Node(3)
	three2 = Node(3)
	three3 = Node(3)
	four = Node(4)
	five = Node(5)
	six = Node(6)
	bindNodes(one, two)
	bindNodes(two, three)
	bindNodes(three, four)
	bindNodes(four, five)
	linkedList.head = one
	linkedList.tail = five

	printLinkedList(linkedList.head)    # None<->1<->2<->3<->4<->5<->None
"""


class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.is_sorted = False

    def addNode(self, node):
        self.setTail(node)

    def setHead(self, node):
        if self.head == None:
            self.tail = node
            self.head = node
        else:
            self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.tail == None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node
        nodeToInsert.prev = node.prev
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        node = self.head
        counter = 1
        while node is not None and counter != position:
            node = node.next
            counter += 1

        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev
        self.removeHelperBindings(node)

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return True
            node = node.next
        return False

    def removeHelperBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
        # node.value = None

    def printLinkedList(self):
        node = self.head
        print("None", end="<->")
        while node is not None:
            print(node.value, end="<->")
            node = node.next
        print("None")

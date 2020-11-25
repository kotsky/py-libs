"""Queue implementation: FIFO

In this sheet, FIFO is implemented by using Singly Linked List:
	- Simple Stack with methods:
		add() - to add element in O(1) Time
		peek() - to check the last element in O(1) Time
		pop() - to delete and return the last element in O(1) Time
		is_empty() - boolean check if the stack is empty
		printChain() - print the chain out, where 1st element if first to out,
		and last element is last to out.
"""
class Queues:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.old = None
        self.recent = None

    def add(self, value):
        new_node = self.Node(value)
        if not self.old:
            self.old = new_node
            self.recent = self.old
        else:
            self.recent.next = new_node
            self.recent = self.recent.next

    def peek(self):
        return self.old.value if self.old is not None else None

    def pop(self):
        node_to_return = self.old
        if self.old:
            self.old = self.old.next
        return node_to_return.value if node_to_return is not None else None

    def is_empty(self):
        return self.old is None

    def printChain(self):
        symbol = '<-'
        node = self.old
        while node is not None:
            print(node.value, end=symbol)
            node = node.next
        print()
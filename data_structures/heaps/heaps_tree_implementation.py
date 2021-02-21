"""Min-Heap tree structure

Thin Min-Heap implementation is based on pure binary tree structure
with certain balancing optimisation by using additional attribute 
direction.

Min-Heap methods:
	- class MinHeap() - Build Min-Heap from an any array with
	integers with a complexity O(N) Time / O(N) Space
	- peek() - check root of that heap
	- insert() - insert value
	- pop() - return and delete min head
	- is_empty() - check if heap is empty

	Example:

		INSERT = "insert"
		REMOVE = "remove"
		PEEK = "peek"
		BUILD = "build"


		def main():

			min_heap = MinHeap()

			while 1:
				user_input = input()
				user_commands = user_input.split(" ")
				command = user_commands[0]
				try:
					value = int(user_commands[1])
				except:
					value = None

				if command == INSERT:
					min_heap.insert(value)
					print("Added ", value)
				elif command == PEEK:
					print("Peek is ", min_heap.peek())
				elif command == REMOVE:
					min_heap.pop()
					print("Removed. New peek is ", min_heap.peek())
				elif command == BUILD:
					array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
					min_heap.build(array)
					min_heap.insert(9)
					min_heap.insert(-200)
					print(len(min_heap))
					while not min_heap.is_empty():
						output = min_heap.pop()
						print("Removed ", output)


		if __name__ == '__main__':
			# app.run(main)
			main()
	
"""



LEFT = 0
RIGHT = 1


class MinHeapNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.direction = LEFT

    def __str__(self):
        return repr(self.value)

    def flip_direction(self):
        self.direction = ~self.direction


class MinHeap:

    def __init__(self, array=None):
        self.root = None
        self.count = 0
        if array is not None:
            self.build(array)

    def build(self, array):
        for value in array:
            self.insert(value)

    def __len__(self):
        return self.count

    def __del__(self):
        pass

    def insert(self, value):

        def swap_values(node1, node2):
            node1.value, node2.value = node2.value, node1.value

        new_node = MinHeapNode(value)
        self.count += 1
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        is_completed = False
        while not is_completed:
            current_node.flip_direction()
            if current_node.value > new_node.value:
                swap_values(current_node, new_node)
            if current_node.direction == LEFT:
                if current_node.left is None:
                    current_node.left = new_node
                    is_completed = True
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    is_completed = True
                else:
                    current_node = current_node.right

    def peek(self):
        return self.root

    def is_empty(self):
        return self.count == 0

    def pop(self):
        if self.count == 0:
            return None
        self.count -= 1
        value = self.root.value
        self.fix_tree()
        return value

    def fix_tree(self):

        def swap_values(node1, node2):
            node1.value, node2.value = node2.value, node1.value

        current_node = self.root
        parent_node = None
        current_node.value = None
        while current_node.left is not None or current_node.right is not None:
            if current_node.left is not None and current_node.right is not None:
                if current_node.left.value <= current_node.right.value:
                    parent_node = current_node
                    current_node = current_node.left
                else:
                    parent_node = current_node
                    current_node = current_node.right
            elif current_node.left is not None:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right
            swap_values(parent_node, current_node)

        if parent_node is None:
            self.root = None
        else:
            if parent_node.left == current_node:
                parent_node.left = None
            else:
                parent_node.right = None



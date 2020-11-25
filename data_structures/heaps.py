"""Min and Max Heaps implementation/classes

Min-Heap
	- class MinHeap() - Build Min-Heap from an any array with
	integers with a complexity O(N) Time / O(N) Space
	- peek() - check root of that heap
	- insert() - insert value
	- printHeap() - print that heap
	- siftUp() - move element up to the root if posiible
	- siftDown() - move element down from the root if possible
	- pop(idx) - return and delete value at 'idx'
	- is_empty() - check if heap is empty

	Example:
		# only integers
		any_array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
		min_head = MinHeap(any_array)
		min_head.printHeap()
		min_head.pop(2)
		min_head.printHeap()
		min_head.pop(0)
		min_head.printHeap()
	
	
Max-Heap
	- class MinHeap() - Build Min-Heap from an any array with
	integers with a complexity O(N) Time / O(N) Space
	- peek() - check root of that heap
	- insert() - insert value
	- printHeap() - print that heap
	- siftUp() - move element up to the root if posiible
	- siftDown() - move element down from the root if possible
	- pop(idx) - return and delete value at 'idx'
	- is_empty() - check if heap is empty
	
	Example:
		# only integers
		any_array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
		min_head = MinHeap(any_array)
		min_head.printHeap()
		min_head.pop(2)
		min_head.printHeap()
		min_head.pop(0)
		min_head.printHeap()

# TODO
    def drawHeap(self)

"""


class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap(self.heap)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index)
            child_index -= 2
            parent_index = (child_index - 1) // 2

    def head(self):
        return self.heap[0]

    def is_empty(self):
        return self.length() == 0

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, -1)
            value = self.heap.pop()
            self.siftDown(idx)
        return value

    def length(self):
        return len(self.heap)

    def siftDown(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] <= self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] > self.heap[child_two_index] and \
                        self.heap[start_index] > self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] > self.heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def siftUp(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        parent_index = (start_index - 1) // 2
        while parent_index >= 0:
            if self.heap[parent_index] > self.heap[start_index]:
                self.swap(start_index, parent_index)
                start_index = parent_index
                parent_index = (start_index - 1) // 2
            else:
                break

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def printHeap(self):
        for num in self.heap:
            print(num, end=' ')
        print('', end='\n')
		
class MaxHeap:
    def __init__(self, array):
        self.heap = array
        self.buildHeap(self.heap)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index)
            child_index -= 2
            parent_index = (child_index - 1) // 2

    def peek(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)

    def siftDown(self, start_index):
		if start_index < 0:
			start_index = len(self.heap) + start_index
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index] >= self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                elif self.heap[child_one_index] < self.heap[child_two_index] and \
                        self.heap[start_index] < self.heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index] < self.heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def siftUp(self, idx):
		if idx < 0:
			idx = len(self.heap) + idx
        idx_parent = (idx - 1) // 2
        while idx_parent >= 0:
            if self.heap[idx] > self.heap[idx_parent]:
                self.swap(idx, idx_parent)
                idx = idx_parent
                idx_parent = (idx - 1) // 2
            else:
                break

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, -1)
            value = self.heap.pop()
            self.siftDown(idx)
        return value

    def length(self):
        return len(self.heap)

    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def printHeap(self):
        for num in self.heap:
            if type(num) == int:
                print(num, end=' ')
        print('', end='\n')
"""Heap functions

	- ContinuousMedianHandler() class to track meadian value of given values.
	- mergeSortedArrays(arrays) - to merge sorted arrays into one sorted 

"""	
		
import heap from *
		
# Insert: O(lon(N)) T  / O(1) S
# Get Median: O(1) TS
"""
The idea: by using heaps, we split array onto 2 parts, where we track its min and max values.
Then, by knowing length of the array, we can calculate its median by using min-max values
of our heaps.
We do rebalancing all time to keep max-heap and min-heap be one size +-1.
"""

class ContinuousMedianHandler:
    def __init__(self):
        self.max_heap = MaxHeap([])
        self.min_heap = MinHeap([])
        self.median = None

    def insert(self, number):
        if not self.min_heap.length() or number < self.min_heap.peek():
            self.max_heap.insert(number)
        else:
            self.min_heap.insert(number)
        self.rebalance()
        self.updateMedian()

    def getMedian(self):
        return self.median

    def updateMedian(self):
        if self.min_heap.length() > self.max_heap.length():
            self.median = self.min_heap.peek()
        elif self.min_heap.length() < self.max_heap.length():
            self.median = self.max_heap.peek()
        else:
            self.median = (self.max_heap.peek() + self.min_heap.peek()) / 2

    def rebalance(self):
        while abs(self.min_heap.length() - self.max_heap.length()) > 1:
            if self.min_heap.length() > self.max_heap.length():
                head = self.min_heap.pop()
                self.max_heap.insert(head)
            else:
                head = self.max_heap.pop()
                self.min_heap.insert(head)


# O(N*log(K) + K) Time / O(N + K) S
# where N - total number of elements
# K - number of subarrays

def mergeSortedArrays(arrays):
    if not len(arrays):
        return arrays
    
	# O(K) Time & Space
    def createMinHeapFromFirstElement(arrays):
        min_heap = ModifiedMinHeap()
        for i in range(len(arrays)):
            # node_config = [initial_element, sub_array_idx,
            #               initial_idx, sub_array_length]
            node_config = [arrays[i][0], i, 0, len(arrays[i])]
            min_heap.addNode(node_config)
        min_heap.head = min_heap.heap[0]
        return min_heap

    def mergeAndSort(arrays, min_heap):
        merged_array = []
        while min_heap.head is not None:
            head = min_heap.head
            merged_array.append(head.value)
            head.idx += 1
            if head.idx < head.limit:
                head.value = arrays[head.sub_array_idx][head.idx]
                min_heap.siftDown(0)
                min_heap.head = min_heap.heap[0]
            else:
                min_heap.removeHead()
        return merged_array

    class ModifiedMinHeap:
        class MinHeapNode:
            def __init__(self, config):
                value, sub_array_idx, idx, limit = config
                self.value = value
                self.sub_array_idx = sub_array_idx
                self.idx = idx
                self.limit = limit

        def __init__(self):
            self.heap = []
            self.head = None

        def addNode(self, node_config):
            node = self.MinHeapNode(node_config)
            self.heap.append(node)
            self.siftUp(-1)

        def siftDown(self, start_index):
            heap = self.heap
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2
            while child_one_index < len(heap):
                if child_two_index < len(heap):
                    if heap[child_one_index].value <= heap[child_two_index].value and \
                            heap[start_index].value > heap[child_one_index].value:
                        new_index = child_one_index
                    elif heap[child_one_index].value > heap[child_two_index].value and \
                            heap[start_index].value > heap[child_two_index].value:
                        new_index = child_two_index
                    else:
                        break
                else:
                    if heap[start_index].value > heap[child_one_index].value:
                        new_index = child_one_index
                    else:
                        break
                self.swap(start_index, new_index, heap)
                start_index = new_index
                child_one_index = 2 * start_index + 1
                child_two_index = 2 * start_index + 2

        def removeHead(self):
            if self.head is not None:
                if len(self.heap) > 1:
                    self.swap(0, len(self.heap) - 1, self.heap)
                    self.heap.pop()
                    self.siftDown(0)
                    self.head = self.heap[0]
                else:
                    self.head = None
                    self.heap.pop()

        def siftUp(self, idx):
            if idx < 0:
                idx = len(self.heap) + idx
            while idx > 0:
                parent_idx = (idx - 1) // 2
                if self.heap[idx].value < self.heap[parent_idx].value:
                    self.swap(idx, parent_idx, self.heap)
                    idx = parent_idx
                else:
                    break

        def swap(self, i, j, array):
            array[i], array[j] = array[j], array[i]
    
    search_heap = createMinHeapFromFirstElement(arrays)
    merged_sorted_array = mergeAndSort(arrays, search_heap)
    return merged_sorted_array
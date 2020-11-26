"""Array Merge functions

	- merge_sorted_arrays(arrays) - to merge sorted arrays into one sorted 

"""


# O(N*log(K) + K) Time / O(N + K) S
# where N - total number of elements
# K - number of subarrays

def merge_sorted_arrays(arrays):

    if not len(arrays):
        return arrays

    # O(K) Time & Space

    def create_min_heap_from_first_element(arrays):
        min_heap = ModifiedMinHeap()
        for i in range(len(arrays)):
            # node_config = [initial_element, sub_array_idx,
            #               initial_idx, sub_array_length]
            node_config = [arrays[i][0], i, 0, len(arrays[i])]
            min_heap.add_node(node_config)
        min_heap.head = min_heap.heap[0]
        return min_heap

    def merge_and_sort(arrays, min_heap):
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

        def add_node(self, node_config):
            node = self.MinHeapNode(node_config)
            self.heap.append(node)
            self.sift_up(-1)

        def sift_down(self, start_index):
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

        def remove_head(self):
            if self.head is not None:
                if len(self.heap) > 1:
                    self.swap(0, len(self.heap) - 1, self.heap)
                    self.heap.pop()
                    self.sift_down(0)
                    self.head = self.heap[0]
                else:
                    self.head = None
                    self.heap.pop()

        def sift_up(self, idx):
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

    search_heap = create_min_heap_from_first_element(arrays)
    merged_sorted_array = merge_and_sort(arrays, search_heap)
    return merged_sorted_array

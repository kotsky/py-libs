"""Dijkstras Algorithm for positive weights - find the sortest paths to each node

We have verteces with their edges, given in adjustent list "edges", where
each idx relates to its node = 0 -> len(edges)-1. There are destination and
weight to reach this destination at edges[idx] accordingly.

We have a start node. The task is to find the shortest path to each node
from the start node. 

2 key points:
	1) all weights are positive;
	2) there is no loop to itself, means 
	no node is not poiting to itself in edges.

Instead of exploring all possible paths and comparing them, 
we do a sort of BFS with dynamic programming techniques.
To understand which node we should explore at first,
we check which node is the closest one to our start node.
Once we did it, we explore this next node, and try to define
which next node is closest to that current node and so on.

To grab the closest node, we use min_heap which gives O(log(N)) time
of grabbing the closest node to current node. Every time we reduce 
min_heap by exploring nodes, so we don't explore them again.

Instruction:
	1. Creat data structures: 1) visited{} to track visited node and 
	their min length; 2) min_heap[] to track min current path.
	2. Start from start node 	-> add to visited;
								-> compare with others node based on dependencies
	3. Get min from min Heap and its idx and start exploring this new node.
	4 Repeat

Example:
	start = 0	# start node
	edges = [
	[[1, 7]], # node 0: 0->1 with weight 7
	[[2, 6], [3, 20], [4, 3]], # node 1: 1->2 with 6, 1->3 with 20, etc
	[[3, 14]], # node 2
	[[4, 2]], # node 3
	[], # node 4
	[]] % node 5
	print(dijkstras_algorithm(start, edges))
	
	# ============ Output
	[0, 7, 27, 10, -1]
"""

# O(v + e) * log(v) Time / O(v) Space, where
# v - number of nodes, e - dependencies/edges

def dijkstras_algorithm(start, edges):

    # to store visited nodes
    # so we don't explore same nodes twice
    visited_nodes = {}

    array = [float("inf") for x in edges]
    array[start] = 0
    # we build min_heap to grab the closest
    # node in O(log(N)) time instead of O(N)
    # if to work with array
    min_heap = MinHeap(array)
    # we have something like
    # [ [1, 0], [0, inf], [2, inf] ] - [node, distance]
    # if start_node is "1"

    # do until min_heap is not empty -
    # means we explored all nodes
    while not min_heap.is_empty():
        current_closest_node, min_length = min_heap.pop(0)
        if current_closest_node in visited_nodes:
            continue
        visited_nodes[current_closest_node] = min_length
        if min_length == float("inf"):
            continue
        for next_node, length in edges[current_closest_node]:
            min_heap.update(next_node, min_length, length)

    # build output array of shortest path
    # from visited_nodes table
    for node in visited_nodes:
        array[node] = visited_nodes[node] if visited_nodes[node] != float("inf") else -1

    return array


class MinHeap:
    def __init__(self, array):
        # we use idx_data{}, which track where
        # node (as its key) locates in heap.
        # So node_shortest_path = heap[idx_data[node]]
        self.idx_data = {}
        self.heap = array.copy()
        # heap has shape like [[node, shortest_path],[],[]]
        self.build_heap(self.heap)

    def build_heap(self, array):
        start_node_idx = None
        for idx in range(len(array)):
            self.idx_data[idx] = idx
            if array[idx] == 0:
                start_node_idx = idx
            array[idx] = [idx, array[idx]]
        array[0], array[start_node_idx] = array[start_node_idx], array[0]
        self.idx_data[0], self.idx_data[start_node_idx] = self.idx_data[start_node_idx], self.idx_data[0]

    def is_empty(self):
        return self.length() == 0

    def pop(self, idx=0):
        if idx == -1:
            value = self.heap.pop()
        else:
            self.swap(idx, self.length()-1)
            value = self.heap.pop()
            self.sift_down(idx)
        return value

    def length(self):
        return len(self.heap)

    def sift_down(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(self.heap):
            if child_two_index < len(self.heap):
                if self.heap[child_one_index][1] <= self.heap[child_two_index][1] and \
                        self.heap[start_index][1] > self.heap[child_one_index][1]:
                    new_index = child_one_index
                elif self.heap[child_one_index][1] > self.heap[child_two_index][1] and \
                        self.heap[start_index][1] > self.heap[child_two_index][1]:
                    new_index = child_two_index
                else:
                    break
            else:
                if self.heap[start_index][1] > self.heap[child_one_index][1]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def sift_up(self, start_index):
        if start_index < 0:
            start_index = len(self.heap) + start_index
        parent_index = (start_index - 1) // 2
        while parent_index >= 0:
            if self.heap[parent_index][1] > self.heap[start_index][1]:
                self.swap(start_index, parent_index)
                start_index = parent_index
                parent_index = (start_index - 1) // 2
            else:
                break

    def peek(self):
        return self.heap[0]

    def swap(self, i, j):
        element1 = self.heap[i]
        element2 = self.heap[j]
        self.idx_data[element1[0]], self.idx_data[element2[0]] = self.idx_data[element2[0]], self.idx_data[element1[0]]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def update(self, idx_to_update, offset, length):
        heap_idx = self.idx_data[idx_to_update] # grab node_idx at heap
        if heap_idx < self.length():
            # update the shortest_path
            self.heap[heap_idx][1] = min(self.heap[heap_idx][1], offset + length)
            # sift up new possible min value
            self.sift_up(heap_idx)

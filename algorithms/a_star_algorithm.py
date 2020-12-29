'''A star algorithm - find the shortest path

Problem: to define the shortest path from the start point
to the end point on the grid (matrix) with obstacles.
Start point has [start_row, start_col].
End point has [end_row, end_col]

The idea behind is that we do a sort of BFS, but we have certain logic
to decide, which node explore next instead of exploring all nodes
around of the current node. This logic is based on f_score which we
assign to each node during their exploring.
f_score = g_score + h_score, where g - how many steps were done from
the start point to the current point; h - heuristic score, which shows how
far is the current point from the end point:
h_score = |x1 - x2| + |y1 - y2|.

To track optimally and grab fast next node to explore with the lowest f_score
at any given time, we use min heap. in addition, we keep track indexes of nodes 
of min heap placement via hash table.  

To build path from the end pint to the start point, we use attribute node.prev_node,
which shows which node we came from to update its f_score (if f_score_prev was higher).

Example:
    endCol = 1
    endRow = 8
    graph = [
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    startCol = 8
    startRow = 1
    print(a_star_algorithm(start_row, start_col, end_row, end_col, graph))
    #============== Output
    [
    [1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8],
    [7, 8], [8, 8], [9, 8], [9, 7], [9, 6], [9, 5],
    [9, 4], [9, 3], [9, 2], [9, 1], [8, 1]
    ]
    #==============
    # endCol = 0
    # endRow = 3
    # graph = [[1, 0, 0], [1, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 0]]
    # startCol = 2
    # startRow = 0
    # print(a_star_algorithm(start_row, start_col, end_row, end_col, graph))

'''


# O(w * h * log(w * h)) Time / O(w * h) Space, where
# w - width of the graph and h - height of the graph

def a_star_algorithm(start_row, start_col, end_row, end_col, graph):

    def _explore_next_node(node, node_before, heap):
		# node.value means that it's an obstacle "1"
        if node is None or node.is_visited is True or node.value == 1:
            return
        heap.update(node, node_before)

    min_heap = MinHeap([start_row, start_col], [end_row, end_col], graph)

    while not min_heap.is_empty():
        node_to_explore = min_heap.pop()
        # if we come to the end point -> stop
        if node_to_explore.coord == [end_row, end_col]:
            break
        node_to_explore.is_visited = True
        row, col = node_to_explore.coord

		# grab all nodes around
        node_above = min_heap.node_table[row-1][col] if row != 0 else None
        node_below = min_heap.node_table[row+1][col] if row != len(min_heap.node_table)-1 else None
        node_left = min_heap.node_table[row][col-1] if col != 0 else None
        node_right = min_heap.node_table[row][col+1] if col != len(min_heap.node_table[0])-1 else None
		
		# and explore them
        _explore_next_node(node_above, node_to_explore, min_heap)
        _explore_next_node(node_below, node_to_explore, min_heap)
        _explore_next_node(node_left, node_to_explore, min_heap)
        _explore_next_node(node_right, node_to_explore, min_heap)

    return min_heap.get_the_shortest_path() # build path


class Node:
    def __init__(self, row, col, value, h_score):
        self.name = str(row) + ',' + str(col)
        self.coord = [row, col]
        self.value = value
        self.is_visited = False
        self.prev_node = None
        self.f_score = float("inf")
        self.g_score = float("inf")
        self.h_score = h_score

    def update_f_score(self):
        self.f_score = self.g_score + self.h_score


class MinHeap:
    def __init__(self, start_point, end_point, matrix):
        # we transfer matrix into node_table to have all info about each node
        self.node_table = [[Node(x, y, matrix[x][y],
                                 self.get_heuristic_value(x, y, end_point[0], end_point[1]))
                            for y in range(len(matrix[0]))] for x in range(len(matrix))]
		
		# update start point
        self.start_node = self.node_table[start_point[0]][start_point[1]]
        self.start_node.g_score = 0
        self.start_node.update_f_score()
		
		# update end point
        self.end_node = self.node_table[end_point[0]][end_point[1]]
		
		# add start point to be explore first
        self.node_idx_in_heap = {self.start_node.name: 0}
        # [node, its f_score] / min_heap by f_score
        self.heap = [[self.start_node, self.start_node.f_score]]

    def update(self, current_node, prev_node):
        if current_node.f_score == float("inf"):
            # we exploring for the first time the 
            # current node
            current_node.g_score = prev_node.g_score + 1
            current_node.update_f_score()
            current_node.prev_node = prev_node
            self.add(current_node)
        elif current_node.g_score > prev_node.g_score + 1:
            # it's the situation when we could come to the 
            # current node earlier
            current_node.g_score = prev_node.g_score + 1
            current_node.update_f_score()
            current_node.prev_node = prev_node
            # update f_score in respective min_heap[node]
            self.heap[self.node_idx_in_heap[current_node.name]][1] = current_node.f_score
            self.sift_up(self.node_idx_in_heap[current_node.name])

    def add(self, node):
        # add node to the end of min_heap
		self.heap.append([node, node.f_score])
		# add node to track table as the last index in min_heap
        self.node_idx_in_heap[node.name] = self.length()-1
		# sift up its node in min_heap by f_score
        self.sift_up(self.node_idx_in_heap[node.name])

    def is_empty(self):
        return self.length() == 0

    def get_heuristic_value(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)

    def pop(self, idx=0):
        # if idx == -1:
        #     node, _ = self.heap.pop()
        # else:
        self.swap(idx, self.length()-1)
        node, _ = self.heap.pop()
		# any time we pop the node from min_heap,
		# we need to remove it from track table as well
        del self.node_idx_in_heap[node.name]
        self.sift_down(idx)
        return node

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
        element1 = self.heap[i][0].name
        element2 = self.heap[j][0].name
        self.node_idx_in_heap[element1], self.node_idx_in_heap[element2] = \
            self.node_idx_in_heap[element2], self.node_idx_in_heap[element1]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def get_the_shortest_path(self):
        if self.end_node.prev_node is not None:
            return self.build_the_shortest_path()
        return []

    def build_the_shortest_path(self):
        path = []
        node = self.end_node
        while node.prev_node is not None:
            path.append(node.coord)
            node = node.prev_node
        path.append(node.coord)
        return path[::-1]

"""Graph

The Graph classe below is for
build graphs from list/array [1, 2, 3, 4],
each of those numbers (#job) has dependencies
as follows:
[[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]],
which means #1 1 <- 2 etc..

Example:
    vertices = [1, 2, 3, 4]
    edges = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]
    graph = Graph(vertices, edges)
    print(graph.breadth_first_search(3))
    print(graph.depth_first_search(3))
"""


class Graph:
    def __init__(self, values, dependencies):
        self.nodes = []
        self.graph = {}
        for value in values:
            self.add_node(value)
        for dep, value in dependencies:
            self.add_dep(value, dep)

    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.dependencies = []
            self.visited = False

    def add_node(self, value):
        self.graph[value] = self.GraphNode(value)
        self.nodes.append(self.graph[value])

    def get_node(self, value):
        if value not in self.graph:
            self.add_node(value)
        return self.graph[value]

    def add_dep(self, value, dep):
        value_node = self.get_node(value)
        dep_node = self.get_node(dep)
        value_node.dependencies.append(dep_node)

    # O(v + e) T / O(v) S
    def depth_first_search(self, start_node_value):
        start_node = self.get_node(start_node_value)

        def _depth_first_search_helper(node, order):
            if node.visited:
                return
            node.visited = True
            order.append(node.value)
            node.visited = True
            for dep in node.dependencies:
                _depth_first_search_helper(dep, order)
            return order

        order = _depth_first_search_helper(start_node, [])
        self.unvisit_nodes()
        return order

    def unvisit_nodes(self):
        for node in self.nodes:
            node.visited = False

    # O(v + e) T / O(v) S
    def breadth_first_search(self, start_node_value):
        start_node = self.get_node(start_node_value)
        table = {start_node: True}
        order = [start_node]
        current_pointer = 0
        while current_pointer < len(order):
            node_to_explore = order[current_pointer]
            for dep in node_to_explore.dependencies:
                if dep not in table:
                    table[dep] = True
                    order.append(dep)
            current_pointer += 1

        for idx in range(len(order)):
            node = order[idx]
            order[idx] = node.value
        return order


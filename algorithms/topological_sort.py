"""Topological Sort

Topological Sort Algorithm designed to solve 
the following problem:

you have list of jobs [1, 2, 3, 4].
Each job has certain dependencies as follows:
	job #2 can be completed after 1, 3 and 4 are done;
	job #3 can be complated after 1 and 4 are done.
Dependencies = [[1, 2], [1, 3], [3, 2], [4, 2], [4, 3]]

Return a valid order in which jobs have to be completed.
If there is no, return an empty array.

The idea:
Transform jobs and dependencies to graph format.
We do DFS from each node, assigning to them is_visited
once we appended node to the finale order, and 
assigning is_visiting during local DFS exploring.
If we meet is_visiting node, then we don't have 
possible job order to return.

"""

# import /data_structures/graph

# O(j + d) Time and Space

def topological_sort(jobs, deps):
    job_graph = Graph(jobs, deps)
    sequence = []
    flag = True
    nodes = job_graph.data.keys()

    for node in nodes:
        if flag is False:
            return []
        flag = depth_first_search(job_graph.data[node], sequence, flag)

    job_graph.unvisit_nodes()
    return list(reversed(sequence))


def depth_first_search(root, sequence, flag):
    if root.visited:
        return True

    if not root.visiting:
        root.visiting = True
    else:
        return False

    for dep in root.dependencies:
        flag = depth_first_search(dep, sequence, flag)
        if flag is False:
            return False
    sequence.append(root.value)
    root.visited = True
    return flag
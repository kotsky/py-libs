# Binary Heaps
Min-Heap and Max-Heap are a complete Binary Tree.
In Min-Heap parent node has lower value than its child nodes. But in Max-Heap child nodes has bigger value then their parent node.
Its implementation done by using an array structure: [Heaps](https://github.com/kotsky/py-libs/blob/master/data_structures/heaps.py)

Follow methods are implemented:
- Build Min-Heap from an any array with integers
- peek() - check root of heap
- pop(idx) - remove value at `idx`
- insert() - insert value into that heap
- printHeap() - print that heap
- siftUp() - move element up to the root if posiible (for heap updates)
- siftDown() - move element down from the root if possible (for heap updates)

### Complexity
#### Create
Time: O(N) - math reason / Space: O(N)
#### Insert/Delete/Search
Time: O(log(N)) / Space: O(1)

The attitude between children and parent nodes with array implementation are as follows:
- `parent_index = (child_index - 1) // 2`
- `child_one_index = 2 * parent_index + 1` and `child_two_index = 2 * parent_index + 2`
	
The picture below shows attitude on Max-Heap example:
![Picture](https://github.com/kotsky/py-libs/blob/master/additional_data/pictures/heap_representing.png)


### Heaps Algorithms / Problems / Usage
Heaps can be used in various problems, where we have to track min and/or max values per some data structure like an array efficiently in log(N) time.
There are listed few examples:
1. When we need track a median value of some array, we can create 2 heaps: min and max, each of which give max value from the 1st part of the array and min value from the 2nd part of the array accordingly. Avaraging of these values gives the median value of the array. [Continuous Median Handler](https://github.com/kotsky/py-libs/blob/master/data_structures/memo_repacement_strategies/continuous_median_handler.py)
2. [Merge Sorted Arrays](https://github.com/kotsky/programming-exercises/blob/master/Heap/Merge%20Sorted%20Arrays.py) - Great usage of Min-Heap -> use min heap as a buffer exchange and comparison of smallest numbers from each subarray. It allows you to improve a speed of searching min value between subarrays from K to log(K), where K is a number of subarrays.

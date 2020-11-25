# FILO: Stack
Stack works in FILO and simply can be implemented with an array.

## Complexity
### Create
Time: O(N) / Space: O(N)
### Insert/Delete/Search
Time: O(k) / Space: O(+1)
### Add (append)
Time: O(1) / Space: O(+1)

## Stack variations
There might be different types of stacks, except having common methods like `add()`, `pop()`, `peek()` and `is_empty()`.
- Simple [Stack](https://github.com/kotsky/py-libs/blob/master/data_structures/memo_repacement_strategies/filo.py)
- [MinMax Stack](https://github.com/kotsky/py-libs/blob/master/data_structures/memo_repacement_strategies/filo.py) - to track min and max values -> to do that, we have additional min and max stacks, where we track min and max values at each index along common stack array.


## Usage
Stacks are often useful in certain recursive algorithms. Sometimes you need to push some data in your memory, but then remove by returning back recursively.
Also, stacks can be used to implement recursive algorithm iteratively.

Another usage of stacks is to save elements in its initial order, and then delete them in backward. It can be used for [tracking Close and Open brackets](https://github.com/kotsky/programming-exercises/blob/master/Stacks%20And%20Queues/Balanced%20Brackets.py).

Or, when you need to simplify something (like long path) into shorter version, like [Shorter Path](https://github.com/kotsky/programming-exercises/blob/master/Stacks%20And%20Queues/Shorten%20Path.py).

# FIFO: Queue
[Queue](https://github.com/kotsky/py-libs/blob/master/data_structures/memo_repacement_strategies/fifo.py) works in FIFO and simply can be implemented with a Singly Linked List.
Be aware that it's too easy to mess up the first and last nodes, so check them twice.

Queue is used in Breadth-first search or other technics, where at first you append other nodes to explore, and then explore  those nodes in order of adding them to queue.
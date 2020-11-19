# Linked List (LL)
Python implementation: [Singly Linked List](https://github.com/kotsky/py-libs/blob/master/linked_list/singly_linked_list.py) and [Doubly  Linked List](https://github.com/kotsky/py-libs/blob/master/linked_list/doubly_linked_list.py)
There is an advice to keep track a LL head and LL tail no matter with LL you are using.
The tail (tail.next) gives instant node appending in the end of LL.
###Visualisation: 
Singly LL: `None->1->2->3->4->5->None`
Doubly LL: `None<->1<->2<->3<->4<->5<->None`

## Complexity
### Create/Copy
Time: O(N) / Space: O(N)
### Get/Insert/Delete/Search (GIDS)
Time: O(i) / Space: O(1), where i - node index
The beauty of LL is that you just need to reassign node before and node after to complete GIDS operation in O(1) Time.
But at first you need to traverse LL to find that node.

## Some code
```
class LLNode:
    def __init__(self, value):
        self.value = value
        #self.prev = None	# optional: for Doubly LL
        self.next = None
```
## Usage & Algorithms
LL is great to use when you have to track certain order of values/nodes, and you need to keep tracking head (start node) and tail (end node) of LL. For instance, LL is used to implement queues: FIFO, etc.
A lot of problems can be solved by traversing and counting LL nodes.
For instance, to delete K node from the end - count node to the end, find total number of nodes and then subtract K from it to define the node, which you have to delete/modify.
For other problems, you might use 2-3 (3 for [reversing](https://github.com/kotsky/py-libs/blob/master/linked_list/Reverse%20LL.py)) pointers with different node's steps at each iteration of traversing.
The biggest difficulties are to assign previous and next nodes and handle head & tail properly.

Tips: 
- Try to visualize nodes and their relations. Then, draw a solution with arrows.
- Remember about null pointer.
- Update Head and Tail if needed.
- A lot of problems can be solved in place (no extra memory use).


### LRU Cahce
Implementation of a [Least Recently Used cache](https://github.com/kotsky/py-libs/blob/master/linked_list/lru_cache.py), which was implemented with a doubly LL.

### Runner technique
You iterate LL with 2 pointers simultaneously, with one ahead other (fast and slow pointers).

#### Find loop
In your LL you might have a loop:
![Picture](https://github.com/kotsky/py-libs/blob/master/linkedlist/LL internal loop.png)
To define it, start traversing with 2 pointers, where every 1 iteration 1st one has step 1 (slow pointer) and 2nd one has step 2 (fast pointer).
If pointers meet at certain point (at node 2*N), then you will have a loop. Better to drawn it by yourself.
Example: [Find a loop](https://github.com/kotsky/py-libs/blob/master/linked_list/Find%20Loop.py)

#### Factorial replacement
`a1->a2->...->an->b1->..->bn` transform to `a1->b1->..->an->bn` - traverse with 2 pointers as in Find Loop above. When fast pointer hits the end point, slow pointer is at the middle. Then, return back fast pointer and do reassigning between slow and fast pointers.

### Rearrange LL
Sometimes, when you need to rebuild LL based on some K value, it's nice to split LL onto 3 parts, build each separated LL (node.value < k), (node.value = k) and (node.value > k). Then, combine 3 parts into one finale LL.
Be aware, that there might be duplicates or no existing of k value node.
Example: [Rearrange LL](https://github.com/kotsky/py-libs/blob/master/linked_list/Rearrange%20Linked%20List.py)
#### Palindrome
Split linked list on 2 parts and check node by node. Example: [SLL Palindrome Check](https://github.com/kotsky/programming-exercises/tree/master/LinkedList/Linked List Palindrome.py)



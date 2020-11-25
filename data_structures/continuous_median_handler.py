"""ContinuousMedianHandler() class to track meadian value of given values.
	
Methods:
	- Insert: O(lon(N)) T  / O(1) S
	- Get Median: O(1) TS

The idea: by using heaps, we split array onto 2 parts, where we track its min and max values.
Then, by knowing length of the array, we can calculate its median by using min-max values
of our heaps.
We do rebalancing all time to keep max-heap and min-heap be one size +-1.


"""	
		
import heap from *


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

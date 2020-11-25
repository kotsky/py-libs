"""Stack implementation: FILO

In this sheet, the following stack are implemented:
	- Simple Stack with methods:
		add() - to add element in O(1) Time
		peek() - to check the last element in O(1) Time
		pop() - to delete and return the last element in O(1) Time
		is_empty() - boolean check if the stack is empty
	- Min Max Stack - to track min and max of the stack
		add() - to add element in O(1) Time
		peek() - to check the last element in O(1) Time
		pop() - to delete and return the last element in O(1) Time
		is_empty() - boolean check if the stack is empty
		getMin() - return min in O(1) Time 
		getMax() - return max in O(1) Time
"""

class Stack:
    def __init__(self):
        self.data = []

    def add(self, value):
        self.data.append(value)

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data

    def pop(self):
        return self.data.pop()


class MinMaxStack:
    def __init__(self):
        self.data = []
        self.min = []
        self.max = []

    def peek(self):
        return self.data[-1] if len(self.data) > 0 else None

    def pop(self):
        self.min.pop()
        self.max.pop()
        return self.data.pop() if len(self.data) > 0 else None

    def push(self, number):
        if len(self.data) > 0:
            self.max.append(max(number, self.max[-1]))
            self.min.append(min(number, self.min[-1]))
        else:
            self.max.append(number)
            self.min.append(number)
        self.data.append(number)

    def getMin(self):
        return self.min[-1] if len(self.data) > 0 else None

    def getMax(self):
        return self.max[-1] if len(self.data) > 0 else None

    def is_empty(self):
        return not self.data
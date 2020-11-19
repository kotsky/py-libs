"""
LRUCache is a class to save key-value pairs (pairs) and to track these pairs.
Once quantity of pairs exceeds maxSize, the oldest pair will be deleted
and after that new pair will be added. 

Methods:
	1. Create LRUCache: new_cache = LRUCache(10)  # 10 - maxSize
	2. new_cache.insertKeyValuePair(key, value)   # Time O(1)
	3. new_cache.getValueFromKey(key)			  # returns value of particular key - Time O(1)
	4. new_cache.getMostRecentKey()				  # returns the most recent used key - Time O(1)
	
Implemented with Doubled LinkedList.

Example:
	
	lruCache = LRUCache(1)
	print(lruCache.getValueFromKey("a"))
	lruCache.insertKeyValuePair("a", 1)
	print(lruCache.getValueFromKey("a"))
	lruCache.insertKeyValuePair("a", 9001)
	print(lruCache.getValueFromKey("a"))
	lruCache.insertKeyValuePair("b", 2)
	print(lruCache.getValueFromKey("a"))
	print(lruCache.getValueFromKey("b"))
	lruCache.insertKeyValuePair("c", 3)
	print(lruCache.getValueFromKey("a"))
	print(lruCache.getValueFromKey("b"))
	print(lruCache.getValueFromKey("c"))


	# lruCache = LRUCache(4)
	# lruCache.insertKeyValuePair("a", 1)
	# lruCache.insertKeyValuePair("b", 2)
	# lruCache.insertKeyValuePair("c", 3)
	# lruCache.insertKeyValuePair("d", 4)
	# print(lruCache.getValueFromKey("a"))
	# lruCache.insertKeyValuePair("e", 5)
	# print(lruCache.getValueFromKey("a"))
	# print(lruCache.getValueFromKey("b"))
	# print(lruCache.getValueFromKey("c"))
"""

class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.current_size = 0
        self.cache = {}
        self.fifo = DDL()

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.current_size < self.maxSize:
                self.current_size += 1
            else:
                head = self.fifo.head
                if head.key in self.cache:
                    del self.cache[head.key]
                self.fifo.removeHead()
            node = DLLNode(key, value)
            self.fifo.addNode(node)
            self.cache[key] = node
        else:
            temp_node = self.cache[key]
            self.fifo.removeBinding(temp_node)
            temp_node.value = value
            self.fifo.addNode(temp_node)

    def getValueFromKey(self, key):
        if key not in self.cache:
            return None
        else:
            node = self.cache[key]
            if node == self.fifo.head:
                self.fifo.removeHead()
            else:
                self.fifo.removeBinding(node)
            self.fifo.addNode(node)
            return node.value

    def getMostRecentKey(self):
        return self.fifo.tail.key if self.fifo.tail is not None else None


class DDL:
    def __init__(self):
        self.tail = None
        self.head = None

    # Insert to the tail
    # Unbind head
    def addNode(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.head.next = None
            self.head.prev = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def removeBinding(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def removeHead(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head.next
            self.removeBinding(self.head)
            self.head = temp_node


class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        # self.data = [self.value, self.prev_node, self.next_node]

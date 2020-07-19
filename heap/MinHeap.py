# MinHeap + buildHeap from an array
# siftDown, siftUp, peek, remove, and insert methods.

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        child_index = len(array) - 1
        parent_index = (child_index - 1) // 2
        while parent_index >= 0:
            self.siftDown(parent_index, array)
            child_index -= 2
            parent_index = (child_index - 1) // 2
        return array

    def siftDown(self, start_index, heap):
        child_one_index = 2 * start_index + 1
        child_two_index = 2 * start_index + 2
        while child_one_index < len(heap):
            if child_two_index < len(heap):
                if heap[child_one_index] <= heap[child_two_index] and \
                        heap[start_index] > heap[child_one_index]:
                    new_index = child_one_index
                elif heap[child_one_index] > heap[child_two_index] and \
                        heap[start_index] > heap[child_two_index]:
                    new_index = child_two_index
                else:
                    break
            else:
                if heap[start_index] > heap[child_one_index]:
                    new_index = child_one_index
                else:
                    break
            self.swap(start_index, new_index, heap)
            start_index = new_index
            child_one_index = 2 * start_index + 1
            child_two_index = 2 * start_index + 2

    def siftUp(self, start_index, heap):
        parent_index = (start_index - 1) // 2
        while parent_index >= 0:
            if heap[parent_index] > heap[start_index]:
                self.swap(start_index, parent_index, heap)
                start_index = parent_index
                parent_index = (start_index - 1) // 2
            else:
                break

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, -1, self.heap)
        to_remove = self.heap.pop()
        self.siftDown(0, self.heap)
        return to_remove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

    def printHeap(self):
            for num in self.heap:
                print(num, end=' ')
            print('', end='\n')

''' 
# TODO
    def drawHeap(self):
        size = len(self.heap)+1
        to_draw = []
        for i in range(size):
            to_draw.append([' ']*size*2)

        i = 0
        offset = 0
        space = len(self.heap*2)
        level = 1
        while i < len(self.heap)-1:

            line = ' ' * int(30 - level * 3 - pow(1.5, level))

            while i < pow(2, level)-1 and i < len(self.heap)-1:
                line += str(self.heap[i])
                line += ' ' * (7 - level)
                #line2 += '/  \\   '
                i += 1

            #to_draw.append(line)
            #to_draw.append(line2)
            print(line)
            #print(line2)

            level += 1

            space = len(self.heap*2) - level * 2

'''

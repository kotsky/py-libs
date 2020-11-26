"""
In this sheet, sorted algorithms are implemented in the most 
optimal way.
The following list:
    Merge Sort
    Heap Sort
    Quick Sort
    Selection Sort
    Insertion Sort
    Bubble Sort
"""

# Avg: Time O(N*log(N)) / Space O(N)
# Worst: Time O(N*log(N)) / Space O(N)
# Idea:
# Create auxiliary array, where you can 
# store intermediate elements. 
# Recursively, divide array/subarrays until 
# you have only 1-2 elements, and then do
# their swapping, and then merge (doMerge) 
# these subarrays on each recursive level.

def mergeSort(array):
    def mergeSubarrays(merge_array, additional_array, start_idx, end_idx):
        if end_idx - start_idx < 1:
            return
        middle_idx = (end_idx + start_idx) // 2
        mergeSubarrays(additional_array, merge_array, start_idx, middle_idx)
        mergeSubarrays(additional_array, merge_array, middle_idx + 1, end_idx)
        doMerge(merge_array, additional_array, start_idx, middle_idx + 1, end_idx)

    def doMerge(merge_array, additional_array, start_one, start_two, end_idx):
        p1 = start_one
        p2 = start_two
        p0 = p1
        while p1 < start_two and p2 <= end_idx:
            if additional_array[p1] > additional_array[p2]:
                merge_array[p0] = additional_array[p2]
                p2 += 1
            else:
                merge_array[p0] = additional_array[p1]
                p1 += 1
            p0 += 1
        while p1 < start_two:
            merge_array[p0] = additional_array[p1]
            p1 += 1
            p0 += 1
        while p2 <= end_idx:
            merge_array[p0] = additional_array[p2]
            p2 += 1
            p0 += 1

    if not len(array) or len(array) <= 1:
        return array
    else:
        merge_array = array
        additional_array = array.copy()
        mergeSubarrays(merge_array, additional_array, 0, len(array) - 1)
        return merge_array


# Avg: Time O(N*log(N)) / Space O(1)
# Worst: Time O(N*log(N)) / Space O(1)
# Idea:
# Convert array to min heap and use log(N) heap
# property to find min N times of subarray N

def heapSort(array):
    def buildHeap(array):
        for i in range(len(array) - 1, 0, -2):
            parent_idx = (i - 1) // 2
            siftDown(array, parent_idx, len(array) - 1)
        return array

    def siftDown(array, parent_idx, end_idx):
        while parent_idx >= 0:
            child_one = 2 * parent_idx + 1
            child_two = 2 * parent_idx + 2
            if child_one > end_idx:
                break
            if child_two > end_idx:
                if array[parent_idx] < array[child_one]:
                    swap(array, parent_idx, child_one)
                break
            if array[parent_idx] < max(array[child_one], array[child_two]):
                if array[child_one] >= array[child_two]:
                    swap(array, parent_idx, child_one)
                    parent_idx = child_one
                else:
                    swap(array, parent_idx, child_two)
                    parent_idx = child_two
            else:
                break

    if len(array) < 2:
        return array
    array = buildHeap(array)
    start_idx = 0
    end_idx = len(array)-1
    while (end_idx - start_idx) > 0:
        siftDown(array, start_idx, end_idx)
        swap(array, start_idx, end_idx)
        end_idx -= 1
    return array


# Avg: Time O(N*log(N)) / Space O(log(N))
# Worst: Time O(N^2) / Space O(log(N))
# Idea:
# You have 3 pointers: pivot, left and right.
# You compare left and right with pivot
# and then swap left or right vs pivot accordingly,
# depends on certain condition. Once you swapped,
# you have subarrays from the left and from the
# right respect to the pivot. Pivot element is in
# a write order. Now, do quickSort for these
# 2 subarrays.

def quickSort(array):
    def sortHelper(array, start_idx, end_idx):
        if end_idx <= start_idx:
            return

        pivot = start_idx
        start_idx += 1
        list_range = [pivot, end_idx]

        while end_idx >= start_idx:
            if array[start_idx] > array[pivot] > array[end_idx]:
                swap(array, start_idx, end_idx)
            if array[start_idx] <= array[pivot]:
                start_idx += 1
            if array[end_idx] >= array[pivot]:
                end_idx -= 1

        swap(array, pivot, end_idx)
        left_sub_isSmaller = list_range[0] - end_idx < end_idx+1, list_range[1]

        if left_sub_isSmaller:
            sortHelper(array, list_range[0], end_idx)
            sortHelper(array, end_idx+1, list_range[1])
        else:
            sortHelper(array, end_idx+1, list_range[1])
            sortHelper(array, list_range[0], end_idx)

    sortHelper(array, 0, len(array)-1)
    return array


# Avg: Time O(N^2) / Space O(1)
# Worst: Time O(N^2) / Space O(1)
# Idea:
# By traversing, we go through elements and do
# swapping if the element before if greater than
# the element after. If we do at least one swap,
# then we do new traversing until there won't be
# swaps.

def bubbleSort(array):
    if not array:
        return None

    len_array = len(array)

    while True:
        was_swap = False
        index = 0
        while index < (len_array - 1):
            if array[index] > array[index + 1]:
                swap(array, index, index + 1)
                was_swap = True
            index += 1

        if was_swap is False:
            return array
        len_array -= 1


# Avg: Time O(N^2) / Space O(1)
# Worst: Time O(N^2) / Space O(1)
# Idea:
# We try to insert elements before others, if they
# are smaller.

def insertionSort(array):
    for i in range(1, len(array)):

        second = i
        while second != 0:
            if array[second] < array[second - 1]:
                swap(array, second, second-1)
                second -= 1
            else:
                break

    return array


# Avg: Time O(N^2) / Space O(1)
# Worst: Time O(N^2) / Space O(1)
# Idea:
# Every iteration we search for the smallest number
# in remaining subarray, and then do swap with
# respective place in the array.

def selectionSort(array):
    for j in range(len(array) - 1):
        upper_pointer = j
        lower_pointer = j

        for i in range(lower_pointer, len(array)):
            if array[upper_pointer] > array[i]:
                upper_pointer = i

        swap(array, lower_pointer, upper_pointer)

    return array


# Simple swap of elements inside of array

def swap(array, idx_one, idx_two):
    array[idx_one], array[idx_two] = array[idx_two], array[idx_one]

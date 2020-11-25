"""
In this sheet searching algorithms are placed:
    Binary Search -> to find an element in a sorted array
    Quick Select -> to find kth smallest element in the array
    Search In Sorted Matrix -> to find an element in a sorted matrix
"""

# Common binary search:
# Find a target in a sorted array.
# Time O(log(N)) / Space O(1)

def binarySearch(array, target):
    left_pointer = 0
    right_pointer = len(array) - 1
    while right_pointer - left_pointer >= 0:
        index = int((right_pointer + left_pointer) / 2)
        if array[index] == target:
            return index
        elif array[index] < target:
            left_pointer = index + 1
        else:
            right_pointer = index - 1
    return -1

# Return kth smallest element from the array
# Avg: Time O(N) / Space O(1)
# Worst: Time O(N*log(N)) / Space O(1)
# The idea behind is to use quickSort
# technique -> find pivot, place it in
# the appropriate place and check at which
# index it is. Then you might ignore
# some part of your array to find kth element.

def quickselect(array, k):
    if k > len(array):
        print("k is greater than array length")
        return

    start_point = 0
    end_point = len(array) - 1

    while True:
        right = end_point
        pivot = start_point
        left = pivot + 1
        while right >= left:
            if array[left] > array[pivot] > array[right]:
                swap(array, left, right)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1

        if right == k - 1:
            return array[pivot]
        swap(array, pivot, right)
        if right < k - 1:
            start_point = right + 1
        else:
            end_point = right - 1


# Search in sorted matrix: Time O(R + C).
# If no -> return [-1, -1]
# idea: check if target can be in particular
# row by comparing the last element in this
# row. If no -> move to the next row.

def searchInSortedMatrix(matrix, target):
    r = 0
    c = len(matrix[0])-1
    while r < len(matrix) and c >= 0:
        current_point = matrix[r][c]
        if current_point == target:
            return [r, c]
        elif current_point < target:
            r += 1
        else:
            c -= 1
    return [-1, -1]


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

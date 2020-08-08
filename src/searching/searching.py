# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = (end - start) // 2

    # error case
    if start > end or len(arr) < 1:
        return -1

    # base cases
    elif arr[mid] == target:
        # base case
        return mid
    elif start == mid and mid == end:
        # negative base case (not found)
        return -1

    # recursive cases
    elif arr[mid] < target:
        # move search to the right
        start = mid
    elif arr[mid] > target:
        # move search to the left
        end = mid
    mid = (end - start) // 2
    return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

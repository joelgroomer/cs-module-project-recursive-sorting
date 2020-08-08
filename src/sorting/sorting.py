# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    a = 0
    b = 0
    for _ in range(0, elements):
        if a >= len(arrA):
            merged_arr.append(arrB[b])
            b += 1
        elif b >= len(arrB):
            merged_arr.append(arrA[a])
            a += 1
        else:
            if arrA[a] < arrB[b]:
                merged_arr.append(arrA[a])
                a += 1
            else:
                merged_arr.append(arrB[b])
                b += 1
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    # base case
    else:
        half = len(arr) // 2
        arr = merge(merge_sort(arr[0:half]), merge_sort(arr[half:]))

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input


def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

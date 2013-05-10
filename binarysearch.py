# binarysearch.py

def binarysearch(array, target, low, high):
    mid = (low + high) // 2
    if low > high:
        return -1
    elif target == array[mid]:
        return mid
    elif target > array[mid]:
        return binarysearch(array, target, mid+1, high)
    elif target < array[mid]:
        return binarysearch(array, target, low, mid-1)

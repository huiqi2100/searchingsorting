# insertionsort.py

def insertionsort(array):
    for j in range(len(array)):
        num = array[j]
        i = j - 1
        while i >= 0 and array[i] > num:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = num
    return array

# bubblesort.py

def bubblesort(array):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swapped = True

    return array

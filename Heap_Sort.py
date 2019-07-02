########################### Heap Sort############################
import math

def Heapify(Array, n, i):
    '''

    :param Array:
    :param n: Usually size of the array
    :param i: The target root node
    :return:
    '''
    #Heapify the array
    left = 2*i+1
    right = 2*i+2
    largest  = i

    if ((left < n) and (Array[left] > Array[i])):
        largest = left
    if ((right < n) and (Array[right] > Array[largest])):
        largest = right

    #print "largest", Array[largest]

    if largest != i:
        Array[i], Array[largest] = Array[largest], Array[i]  # swap
        Heapify(Array, n, largest)

# Test Heapify
arr1 = [2,1,6,9,5]
Heapify(arr1, 5, 0)
# print arr1

def HeapSort(Array):
    n = len(Array)

    # Build the max heap first
    for i in range(n, -1, -1):
        Heapify(Array, n, i)

    # Extract the root, put it at the end, and heapify the rest
    for j in range(n-1, 0, -1):
        Array[0], Array[j] = Array[j], Array[0]
        Heapify(Array, j, 0)

# Test HeapSort

HeapSort(arr1)
# print arr1

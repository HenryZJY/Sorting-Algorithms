##################### Selection Sort ############################
import math

def SelectionSort(Array):

    for i in range(0, len(Array)-1):
        min_ind = i
        for j in range(i, len(Array)):
            if Array[j] < Array[min_ind]:
                min_ind = j
        # Swap min to the front of the subarray
        temp = Array[min_ind]
        Array[min_ind] = Array[i]
        Array[i] = temp

#Test SelectionSort
# array_1 = [3,2,6,87,54]
# SelectionSort(array_1)
# print array_1

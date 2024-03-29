##########################Shell Sort#####################################
import math

def ShellSort(arr):
    '''
    Divide the array based on gap for several times, and use insert sort every time.
    :param arr:
    :return:
    '''
    gap = len(arr)/2
    while gap > 0:

        for i in range(gap, len(arr), 1):
            # create a hole here
            temp = arr[i]
            # insert sort the gapped array
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j-gap]
                j = j-gap
            # fill the hole
            arr[j] = temp

        gap /= 2

# test Shell Sort
print "----------- Shell Sort ---------------"
arr3 = [2,1,4,7,9,5]
ShellSort(arr3)
print arr3

########################## Insertion Sort #################################
import math

def InsertSort(arr):

    for i in range(1, len(arr), 1):
        # Insert i into the right place in the subarray
        ind = i
        for j in range(i, -1, -1):
            # print "ind", ind
            # print 'j', j
            # print 'arr[ind]', arr[ind], 'arr[j]'  , arr[j]
            if arr[ind] < arr[j]:
                arr[ind], arr[j] = arr[j], arr[ind]
                ind = j
            j -= 1

# Test InsertSort
arr2 = [2,4,1,3,5,56,43]
InsertSort(arr2)
print arr2

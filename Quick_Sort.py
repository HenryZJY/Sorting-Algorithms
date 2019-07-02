#####################Quick Sort########################
import math

def partition(A, low, high):
    '''
    Use a Pivot.
    :param A:
    :param low:
    :param high:
    :return:
    '''
    pivot = A[low]
    i = low + 1
    j = high
    done = False

    while not done:
        while (j >= i and A[j] > pivot):
            print "j", j
            print "A[j]", A[j]
            j -= 1

        while (i <= j and A[i] < pivot):
            print "i", i
            print "A[i]", A[i]
            i += 1

        if i > j:
            done = True

        else:
            print"swap", A[i], A[j]
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

    tem = A[j]
    A[j] = A[low]
    A[low] = tem
    print "list in parititon", A
    return j


# test partition
# b = [5,6,7,4,3,2,1]
# print partition(b,0,6)
a = [2, 4, 7, 1, 3, 10, 5]
# print partition(a, 0, 6)
# print a


def QuickSort_helper(B, low, high):
    if low < high:
        pivot_ind = partition(B, low, high)
        QuickSort_helper(B, low, pivot_ind - 1)
        QuickSort_helper(B, pivot_ind + 1, high)


def QuickSort(L):
    QuickSort_helper(L, 0, len(L) - 1)
    
# test
# QuickSort(a)
# print a

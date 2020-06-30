from math import ceil
from random import randrange
from time import time
# Sorts array of numbers in place
# Input: A - array of numbers, must have length > 1
#        low - index of where to start sorting array
#        high - index of where to split array
#        alpha - variable to split array, 0.5 < alpha < 1
# Output: none
def badSort(A, low, high, alpha):
    n = high - low + 1
    # Base case
    if n == 2 and A[low] > A[high]:
        A[low], A[high] = A[high], A[low]
    elif n > 2:
        m = ceil(alpha * n)
        if n == m:
            m -= 1
        # Sort first part of array
        badSort(A, low, low+m-1, alpha)
        # Sort second part of array
        badSort(A, high-m+1, high, alpha)
        # Sort first part of array again
        badSort(A, low, low+m-1, alpha)

alpha = [2/3, 3/4]
for a in alpha:
    # size of tests
    nums = [10, 20, 30, 40, 50, 60, 70]
    for n in nums:
        # fill array with zeroes
        numArr = [0] * n
        totalTime = 0
        # take the average of 100 trials for each number
        for i in range(100):
            # fill array with random nums between 0 - 10,000
            for i in range(n):
                numArr[i] = randrange(10000)
            # start timer
            start = time()
            # sort array using insert sort
            badSort(numArr, 0, n-1, a)
            # stop timer
            end = time()
            totalTime += (end - start)
        # print timer
        print(str(n) + ' numbers in array with alpha: ' + str(a) + '\tTime taken: ' + str(totalTime/100))
import sys
from math import ceil

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

if len(sys.argv) == 2:
    alpha = int(sys.argv[1][0]) / int(sys.argv[1][2])
    print(alpha)
    # Sets file path
    filepath = 'data.txt'
    # String to write to output file
    newFileStr = ''
    # opens file and stores in fp
    with open(filepath) as fp:
        # reads first line of file
        line = fp.readline()
        # while there are still existing lines
        while line:
            # parse line to strip of \n's an store in array
            nums = [int(x) for x in line.strip('\n').split(' ')]
            # get length of nums
            numslen = nums.pop(0)
            # perform insertion sort on array of nums
            badSort(nums, 0, numslen-1, alpha)
            # for each num in num array, write to output file
            for num in nums:
               newFileStr += str(num) + ' '
            newFileStr += '\n'
            # read next line
            line = fp.readline()

    # write string to output file
    with open('bad.out', 'w') as output:
        output.write(newFileStr)
else:
    print('Run program in format: \'python badsort.py [alpha]\'\nAlpha must be in format int/int (e.g. 2/3), and it must be between 0.5 and 1 (exclusive)');
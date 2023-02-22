#  File: Work.py

# Description: This program takes in values n (total lines of code) and k (productivity factor) from a text file and
# computes the number of lines that need to be written using a linear and binary search

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 10.02.2021

#  Date Last Modified: 10.04.2021

# Import Libraries
import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series(v, k):
    p = 1
    seriesVal = v
    seriesSum = seriesVal
    while seriesVal > 0:
        seriesVal = v // k ** p
        seriesSum += seriesVal
        p += 1
    return seriesSum


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search(n, k):
    if n < k:
        return n
    else:
        for v in range(n):
            seriesSum = sum_series(v, k)
            if seriesSum >= n:
                return v


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search(n, k):
    if n < k:
        return n
    else:
        low = 1
        high = n
        while low <= high:
            middle = (low + high) // 2
            seriesMid = sum_series(middle, k)
            seriesMidLow = sum_series(middle - 1, k)

            if seriesMidLow < n <= seriesMid:
                return middle
            elif seriesMid >= n:
                high = middle
            else:
                low = middle


def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int(line)

    for i in range(num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp = line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()


if __name__ == "__main__":
    main()

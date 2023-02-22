#  File: Spiral.py

#  Description: This program takes in input data from a file, where the first
#               number is the dimension (n) to be used in the making of an
#               n x n 2d matrix. This matrix is constructed as a spiral of
#               numbers in order. The remaining numbers in the file correspond
#               to numbers inside the spiral. The output is the sum of all the
#               numbers adjacent to those numbers, but not including the number.

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 09/05/2021

#  Date Last Modified: 09/06/2021


# Import libraries
import sys


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    if n % 2 == 0:
        n += 1
    elif (n < 1) or (n > 100):
        print("Dimensions out of range")
        sys.exit()
    spiralMatrix = [[0 for x in range(n)] for y in range(n)]    # Create 2d matrix
    value = n**2    # Number to be inserted in cell
    x = n - 1       # x-coordinate
    y = 0           # y-coordinate
    x_high = n - 1  # High x-coordinate
    y_high = n - 1  # High y-coordinate
    x_low = 0       # Low x-coordinate
    y_low = 1       # Low y-coordinate
    direction = "Left"
    while True:
        if value == 0:  # Makes sure spiral ends at 1
            break

        # Move to the left and input value. For first round:
        # X: START: 10 ACTION: x -= 1 END: 0
        # Y: START: 0 ACTION: None END: y+1 (1)
        if direction == "Left":
            spiralMatrix[x][y] = value
            value -= 1
            if x <= x_low:      #End of Row
                direction = "Down"
                y += 1
                x_low += 1
            else:
                x -= 1

        # Move down column. For first round:
        # X: START: 0 ACTION: None END: x+1 (1)
        # Y: START: 1 ACTION: y += 1 END: 10
        elif direction == "Down":
            spiralMatrix[x][y] = value
            value -= 1
            if y >= y_high:     # End of column
                direction = "Right"
                x += 1
                y_high -= 1
            else:
                y += 1

        # Move to right of row. For first round:
        # X: START: 1 ACTION: x += 1 END: x = 10
        # Y: START: 10 ACTION: None END: 10
        elif direction == "Right":
            spiralMatrix[x][y] = value
            value -= 1
            if x >= x_high:     # End of Row
                direction = "Up"
                y -= 1
                x_high -= 1
            else:
                x += 1
        # Move up a column. For first round:
        # X: START: 10 ACTION: None END: x-1 (9)
        # Y: START: 9 ACTION: y -= 1 END: 1
        elif direction == "Up":
            spiralMatrix[x][y] = value
            value -= 1
            if y <= y_low:      # End of Column
                direction = "Left"
                x -= 1
                y_low += 1
            else:
                y -= 1
    # Left for 11   (x -= 1, y = 0)     (x: 10 to 0, y: 0)
    # Down for 10   (x = 0, y -= 1)     (x: 0, y: 1 to 10)
    # Right for 10  (x += 1, y = 10)    (x: 1 to 10, y: 10)
    # Up for 9      (x = 10, y += 1)    (x: 10, y: 9 to 1)

    # Left for 9                        (x: 9 to 1, y: 1)
    # Down for 8                        (x: 1, y: 2 to 9)
    # Right for 8                       (x: 2 to 9, y: 9)
    # Up for 7                          (x: 9, y: 8 to 2)

    # Left: START: 10 ACTION: x -= 1 END: 0
    # Down: START: 0 ACTION: None END: x+1 (1)
    # Right: START: 1 ACTION: x += 1 END: x = 10
    # Up: START: 10 ACTION: None END: x-1 (9)

    # Left: START: 0 ACTION: None END: y+1 (1)
    # Down: START: 1 ACTION: y += 1 END: 10
    # Right: START: 10 ACTION: None END: 10
    # Up: START: 9 ACTION: y -= 1 END: 1
    return spiralMatrix


# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    for i in range(len(spiral)):
        for j in range(len(spiral)):
            if spiral[i][j] == n:
                x, y = i, j
                break
        else:
            continue
        break

    sum_count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                if (0 <= x + i < len(spiral)) and (0 <= y + j < len(spiral)):
                    test = spiral[x + i][y + j]
                    sum_count += spiral[x + i][y + j]

    return sum_count


# Input: None
# Output: Information from text file where n is
#         the spiral dimension and num a list of
#         the numbers to be checked
def read_file():
    file = sys.stdin.read()
    a = file.split("\n")
    n = 0
    nums = []
    i = 0
    for value in a:
        if i == 0:
            n = int(a[i])
            i += 1
        elif a[i]:
            nums.append(int(a[i]))
            i += 1

    return n, nums


def main():

    # read the input file
    n, nums = read_file()

    # create the spiral
    spiralMatrix = create_spiral(n)

    # add the adjacent numbers
    results = []
    for i in nums:
        results.append(sum_adjacent_numbers(spiralMatrix, i))

    # print the result
    print(*results, sep="\n")


if __name__ == "__main__":
    main()

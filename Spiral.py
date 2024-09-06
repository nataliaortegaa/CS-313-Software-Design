#  File: Spiral.py
#  Student Name: Ashley Chen
#  Student UT EID: ac83374
#  Partner Name: Natalia Ortega
#  Partner UT EID: no4432

import sys


# Input: n
# Output:
def get_dimension(in_data):
    pass
    try:
        str_res = in_data.readline()
        if (str_res == ""):
            return "end"
        n = int(str_res)
        return n
    except ValueError:
        print("Invalid data")


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    if n % 2 == 0:
        n += 1

    if n < 1 or n > 100:
        print("Out of Bounds")

    spiral = [[0] * n for _ in range(n)]
    x, y = n // 2, n // 2  # Starting position in the middle
    value = 1

    spiral[y][x] = value

    for step in range(1, n, 2):
        # Move right
        for _ in range(step):
            x += 1
            value += 1
            spiral[y][x] = value

        # Move down
        for _ in range(step):
            y += 1
            value += 1
            spiral[y][x] = value

        # Move left
        for _ in range(step + 1):
            x -= 1
            value += 1
            spiral[y][x] = value

        # Move up
        for _ in range(step + 1):
            y -= 1
            value += 1
            spiral[y][x] = value

    value += 1
    for i in range(1, n):
        spiral[0][i] = value
        value += 1

    return spiral


# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    pass
    n = -1
    while n != "end":
        n = get_dimension(in_data)
        if (n != None and n != "end"):
            print(sum_adjacent_numbers(spiral, n))


# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    pass
    cells_sum = 0
    row_num = 0
    col_num = 0
    # find x and y position of n numbercl
    if n < 1 or n > (len(spiral) ** 2):
        print("0")
    else:
        for x in range(len(spiral)):
            for y in range(len(spiral)):
                if spiral[x][y] == n:
                    row_num = x
                    col_num = y

    # check and add adjacent cells to the sum
    # going right, left, up, down, then corners clockwise from the top right
    for row in range(row_num - 1, row_num + 2):
        for col in range(col_num - 1, col_num + 2):
            if (row < 0 or row >= len(spiral) or col < 0 or col >= len(spiral)):
                pass
            else:
                cells_sum += spiral[row][col]
    return cells_sum - n


# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():
    # set the input source - change to False before submitting
    debug = False
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # use following line for debugging only
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)


if __name__ == "__main__":
    main()
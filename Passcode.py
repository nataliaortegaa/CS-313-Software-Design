# File: Passcode.py
# Description: Given a sequence of number, find length traveled on number pad
# Student Name: Natalia Ortega
# Student UT EID: no4432
# Course Name: CS 313E: Elements of Software Development

import math
import sys

# Input: a list of integers representing the sequence of numbers in a password, 
# len(ptrn) >= 2
# Output: distance traveled on the number pad
def get_distance(pattern):
    total_distance = 0.0

    for i in range(len(pattern) - 1):
        x1, y1 = find_in_keypad(pattern[i])
        x2, y2 = find_in_keypad(pattern[i + 1])

        dx = x2 - x1
        dy = y2 - y1

        distance = (dx ** 2 + dy ** 2) ** 0.5
        total_distance += distance

    return total_distance


# DO NOT Edit Below This Line, except for changing the debug variable when you are done


#  Find the equivilant x,y based on grid concept
def find_in_keypad (num):
    row = (num - 1) // 4
    col = (num - 1) % 4
    return (row, col)

# take an input string and create a list of numbers
def get_pattern (line):
    input_pattern = []
    line = line.split()
    for element in line:
        input_pattern.append(int(element))
    return input_pattern
    
# run the program
def main():
    
    # open file
    debug = False
    if debug:
        in_data = open('passcode.in')
    else:
        in_data = sys.stdin

    # read and process each line until EOF
    line = in_data.readline()
    while line != "":
        pattern = get_pattern(line)
        print(f'Pattern: {pattern}')
        print("Distance: {:.2f}".format(get_distance(pattern)))
        print()
        line = in_data.readline()

if __name__ == "__main__":
    main()
#  File: Work.py
#  Student Name: Natalia Ortega
#  Student UT EID: no4432

import sys
import time



def sum_series(lines_before_coffee, prod_loss):
    if lines_before_coffee < 1:
        return 0
    return lines_before_coffee + sum_series(lines_before_coffee // prod_loss, prod_loss)


def linear_search(total_lines, prod_loss):
    lines_before_coffee = 1
    calls_to_sum_series = 0

    while True:
        calls_to_sum_series += 1
        if sum_series(lines_before_coffee, prod_loss) >= total_lines:
            return lines_before_coffee, calls_to_sum_series
        lines_before_coffee += 1

def binary_search(total_lines, prod_loss):
    low = 1
    high = total_lines
    ideal_lines = total_lines  # Initially set it to the upper limit
    calls_to_sum_series = 0

    while low <= high:
        mid = (low + high) // 2
        calls_to_sum_series += 1
        current_total = sum_series(mid, prod_loss)

        if current_total >= total_lines:
            ideal_lines = mid  # Update the ideal_lines when we find a valid mid
            high = mid - 1     # Try to search for a lower possible mid

        else:
            low = mid + 1

    return ideal_lines, calls_to_sum_series




''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Open input source
    # Change debug to false before submitting
    debug = False
    if debug:
        in_data = open('work.in')
    else:
        in_data = sys.stdin

    # read number of cases
    line = in_data.readline().strip()
    num_cases = int(line)

    for i in range(num_cases):

        # read one line for one case
        line = in_data.readline().strip()
        data = line.split()
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(binary_time),
              "seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print("Elapsed Time:", "{0:.8f}".format(linear_time),
              "seconds")
        print()

        # Comparison
        print("Binary Search was",
              "{0:.1f}".format(linear_time / binary_time),
              "times faster.")
        print()
        print()


if __name__ == "__main__":
    main()

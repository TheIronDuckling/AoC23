# Advent of Code 2023
import os
import sys
import math
from utility.utility import *

# Day 3 -
day = os.path.basename(__file__)[:-3].split("_")[1]

def is_symbol(c:str):
    return not (c.isnumeric() or c == ".")

def pull_numbers_from_line(line):
    numbers = []
    curr_num = ""
    for c in line:
        if c.isnumeric():
            curr_num += c
        else:
            if curr_num != "":
                numbers.append(int(curr_num))
                curr_num = ""
    if curr_num != "":
        numbers.append(int(curr_num))
    return numbers

def run():
    print("==========================================================")
    print("                ADVENT OF CODE 2023: DAY {}                ".format(day))
    print("==========================================================")
    input_filename = "day_{}_in.txt".format(day)
    lines = read_all_lines(os.path.join("inputs", input_filename))
    if len(lines) == 0:
        print("Day {} has no input - Skipping".format(day))
    else:
        # Part 1 =======================================================================================================
        print("=====================   PART 1   =========================")
        result = 0
        numbers = []
        # look for numbers in row
        for y, l in enumerate(lines):
            current_number_start = None
            current_number_end = None
            current_number_characters = ""
            for x, c in enumerate(l):
                if c.isnumeric():
                    if current_number_start is None:
                        current_number_start = x
                    current_number_characters += c
                if (not c.isnumeric()) and current_number_start is not None:
                    current_number_end = x - 1
                    search_x_start = max(current_number_start - 1, 0)
                    search_x_end = min(current_number_end + 1, len(l))
                    line_above = "" if y == 0 else lines[y-1][search_x_start:search_x_end+1]
                    line_below = "" if y+1 == len(lines) else lines[y+1][search_x_start:search_x_end+1]
                    left_and_right = ""
                    if current_number_start > 0:
                        left_and_right += l[current_number_start - 1]
                    if current_number_end + 1 < len(l):
                        left_and_right += l[current_number_end+1]

                    print(current_number_characters)
                    print(line_above + left_and_right + line_below)
                    for s in line_above + line_below + left_and_right:
                        assert isinstance(s, str)
                        if is_symbol(s):
                            print("True")
                            result += int(current_number_characters)
                            numbers.append(int(current_number_characters))
                            break

                    current_number_start = None
                    current_number_end = None
                    current_number_characters = ""
            if current_number_characters != "":
                current_number_end = x - 1
                search_x_start = max(current_number_start - 1, 0)
                search_x_end = min(current_number_end + 1, len(l))
                line_above = "" if y == 0 else lines[y - 1][search_x_start:search_x_end + 1]
                line_below = "" if y + 1 == len(lines) else lines[y + 1][search_x_start:search_x_end + 1]
                left_and_right = ""
                if current_number_start > 0:
                    left_and_right += l[current_number_start - 1]
                if current_number_end + 1 < len(l):
                    left_and_right += l[current_number_end + 1]

                print(current_number_characters)
                print(line_above + left_and_right + line_below)
                for s in line_above + line_below + left_and_right:
                    assert isinstance(s, str)
                    if is_symbol(s):
                        print("True")
                        result += int(current_number_characters)
                        numbers.append(int(current_number_characters))
                        break

                current_number_start = None
                current_number_end = None
                current_number_characters = ""

        print(numbers)
        print(f"Part 1 Result: {result}")
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        result2 = 0
        for y, l in enumerate(lines):
            for x, c in enumerate(l):
                if c == "*":
                    min_x = 0 if x == 0 else x - 1
                    if x == len(l) - 1:
                        # last char
                        max_x = x
                    else:
                        max_x = x+1
                    min_y = 0 if y == 0 else y - 1
                    if y == len(lines) - 1:
                        # last char
                        max_y = y
                    else:
                        max_y = y + 1
                    all_lines = []
                    for y2 in range(min_y, max_y+1):
                        c_min = min_x
                        c_max = max_x
                        sub_line = lines[y2][c_min:c_max+1]
                        while sub_line[0].isnumeric() and c_min != 0:
                            c_min -= 1
                            sub_line = lines[y2][c_min:c_max+1]
                        while sub_line[-1].isnumeric() and c_max != len(lines[y2]):
                            c_max += 1
                            sub_line = lines[y2][c_min:c_max+1]
                        all_lines.append(sub_line)
                    all_surrounding_numbers = []
                    for sl in all_lines:
                        all_surrounding_numbers.extend(pull_numbers_from_line(sl))
                    if len(all_surrounding_numbers) == 2:
                        print(all_lines)
                        print(all_surrounding_numbers)
                        result2 += all_surrounding_numbers[0] * all_surrounding_numbers[1]
        print(f"Part 2 Result: {result2}")
        # ==============================================================================================================
        print("==========================================================")


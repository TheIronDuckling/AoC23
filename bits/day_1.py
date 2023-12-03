# Advent of Code 2023
import os
import sys
import math
from utility.utility import *

# Day 1 - Trebuchet?!
day = os.path.basename(__file__)[:-3].split("_")[1]

valid = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

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
        # all_nums = []
        # for l in lines:
        #     n = [c for c in l if c.isnumeric()]
        #     all_nums.append(int(n[0] + n[-1]))
        # print(sum(all_nums))
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        all_nums_2 = []
        for l in lines:
            line_numbers = []
            for idx, c in enumerate(l):
                if c.isnumeric():
                    line_numbers.append(c)
                else:
                    for w in valid.keys():
                        length = len(w)
                        if l[idx:idx+length] == w:
                            line_numbers.append(valid[w])
                            break
            all_nums_2.append(int(line_numbers[0] + line_numbers[-1]))
        print(sum(all_nums_2))
        # ==============================================================================================================
        print("==========================================================")


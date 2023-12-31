# Advent of Code 2023
import os
import sys
import math
from utility.utility import *

# Day 5 -
day = os.path.basename(__file__)[:-3].split("_")[1]


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

        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")

        # ==============================================================================================================
        print("==========================================================")


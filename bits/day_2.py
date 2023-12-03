# Advent of Code 2023
import os
import sys
import math
from utility.utility import *

# Day 2 -
day = os.path.basename(__file__)[:-3].split("_")[1]

class Round:
    def __init__(self, line):
        self.colors = {}
        self.parse_round(line)

    def parse_round(self, line: str):
        cols = line.split(", ")
        for c in cols:
            self.colors[c.split(" ")[1]] = int(c.split(" ")[0])

class Game:
    def __init__(self, line):
        self.game_number = None
        self.rounds = []
        self.minimum_set = {}
        self.parse_game_line(line)

    def parse_game_line(self, line: str):
        halves = line.split(": ")
        self.game_number = int(halves[0].split(" ")[1])
        results = halves[1]
        rounds = results.split("; ")
        for r in rounds:
            new_round = Round(r)
            self.rounds.append(new_round)
            for c, n in new_round.colors.items():
                if c in self.minimum_set:
                    self.minimum_set[c] = max(new_round.colors[c], self.minimum_set[c])
                else:
                    self.minimum_set[c] = new_round.colors[c]

    def check_if_possible(self, col_dict):
        for r in self.rounds:
            for c in col_dict.keys():
                if c in r.colors.keys() and r.colors[c] > col_dict[c]:
                    return False
        return True

    @property
    def power(self):
        res = 1
        for _, n in self.minimum_set.items():
            res *= n
        return res


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
        all_games = [Game(l) for l in lines]
        check_for = {'red': 12, 'green': 13, 'blue': 14}
        s = 0
        for g in all_games:
            assert isinstance(g, Game)
            if g.check_if_possible(check_for):
                s += g.game_number
        print(s)
        # ==============================================================================================================
        # Part 2 =======================================================================================================
        print("=====================   PART 2   =========================")
        powers = sum([g.power for g in all_games])
        print(powers)
        # ==============================================================================================================
        print("==========================================================")


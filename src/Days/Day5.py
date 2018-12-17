# src/Days/Day5.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day5Puzzle1(Puzzle):
    """
    Day5 Puzzle1 class
    """
    def solve(self):
        print("Day5 - Puzzle1")
        polymer = list(self.input.rstrip())

        resulting_polymer = react(polymer)

        print("Solution: {}".format(str(len(resulting_polymer))))


class Day5Puzzle2(Puzzle):
    """
    Day5 Puzzle2 class
    """
    def solve(self):
        print("Day5 - Puzzle2")
        polymer = list(self.input.rstrip())

        # find the unique units in the polymer
        uniq_units = {}
        for unit in polymer:
            unit = unit.lower()
            if unit in uniq_units:
                uniq_units[unit] += 1
            else:
                uniq_units[unit] = 1

        min_resulting_polymer = len(polymer)    # initialize min length of resulting polymer with initial polymer size

        # loop all unique units, remove them and their uppercase versions too (X/x) from the array
        for unit in sorted(uniq_units):
            new_list = list(filter(unit.__ne__, polymer))               # remove x one
            new_list = list(filter((unit.upper()).__ne__, new_list))    # remove X one

            resulting_polymer = react(new_list)                         # calculate the resulting polymer

            if min_resulting_polymer >= len(resulting_polymer):         # check if it's new minimum
                min_resulting_polymer = len(resulting_polymer)

        print("Solution: {}".format(str(min_resulting_polymer)))


def react(polymer):
    """Fully react operation"""
    resulting_polymer = []

    prev_char = None
    while polymer:                       # loop through the polymer array
        char = polymer.pop(0)            # fetch the first char in the polymer array

        # initialization for
        if prev_char is None:
            prev_char = char
            resulting_polymer.append(char)   # initialize the fixed polymer
            continue

        # control if the chars have the different case but the same char
        if prev_char.lower() == char.lower() and \
                prev_char != char:

            resulting_polymer.pop(-1)          # remove prev char from fixed list i.e. xX destroys itself

            # reset the prev char
            if len(resulting_polymer) >= 1:
                prev_char = resulting_polymer[-1]
            else:
                prev_char = None
        else:
            prev_char = char
            resulting_polymer.append(char)     # append the char to the fixed list

    return resulting_polymer


class Day5(Day):
    """
    Day5 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day5, self).__init__(day_number=5)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day5Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day5Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day4.day {}>".format(self.day_number)

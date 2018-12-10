# src/Days/Day1.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day1Puzzle1(Puzzle):
    """
    Day1 Puzzle1 class
    """
    def solve(self):
        print("Day1 - Puzzle1")
        freq_changes = self.input.splitlines()

        current_freq = 0
        for change in freq_changes:
            current_freq += int(change)

        print("Solution: {}".format(str(current_freq)))


class Day1Puzzle2(Puzzle):
    """
    Day1 Puzzle2 class
    """
    def solve(self):
        print("Day1 - Puzzle2")
        freq_changes = self.input.splitlines()

        current_freq = 0
        occurences = {}
        loop = True

        while loop:
            for change in freq_changes:
                if current_freq in occurences:
                    occurences[current_freq] += 1
                else:
                    occurences[current_freq] = 1

                if occurences[current_freq] == 2:
                    loop = False
                    break

                current_freq += int(change)

            if not loop:
                break

        print("Solution: {}".format(str(current_freq)))


class Day1(Day):
    """
    Day1 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day1, self).__init__(day_number=1)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day1Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day1Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day1.day {}>".format(self.day_number)

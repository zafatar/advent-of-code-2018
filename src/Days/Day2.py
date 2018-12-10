# src/Days/Day2.py

from src.Day import Day
from src.Puzzle import Puzzle


class Day2Puzzle1(Puzzle):
    """
    Day2 Puzzle1 class
    """
    def solve(self):
        print("Day2 - Puzzle1")
        box_ids = self.input.splitlines()   # read the list of device IDs
        total_counts = {}

        for box_id in box_ids:
            chars = list(box_id)            # get the list of chars in the box ID

            count = {}                      # count characters - reset for each box ID
            for char in chars:
                count[char] = chars.count(char)

            seen = {}                       # keep track of seen numbers in on box ID
            for char, count in count.items():
                if count in seen:
                    continue

                seen[count] = 1             # set char count as seen and add it to total count
                if count in total_counts:
                    total_counts[count] += 1
                else:
                    total_counts[count] = 1

        # check sum is the multiplication of count 2 and count 3
        checksum = total_counts[2] * total_counts[3]

        print("Solution: {}".format(str(checksum)))


class Day2Puzzle2(Puzzle):
    """
    Day2 Puzzle2 class
    """
    def solve(self):
        print("Day2 - Puzzle2")
        box_ids = self.input.splitlines()

        common_letters = None
        for box_a_index, box_a_id in enumerate(box_ids):
            for box_b_index, box_b_id in enumerate(box_ids[box_a_index+1:]):

                diff_positions = Day2Puzzle2._compare_box_ids(box_a_id, box_b_id)
                if len(diff_positions) == 1:
                    common_letters = Day2Puzzle2._clean_box_id(box_a_id, diff_positions)

        print("Solution: {}".format(common_letters))

    @staticmethod
    def _compare_box_ids(box_a_id, box_b_id):
        """Compares 2 strings and returns the list of positions with different chars"""
        list_of_chars_box_a = list(box_a_id)
        list_of_chars_box_b = list(box_b_id)

        diff_positions = []
        # Assumption: 2 strings have the same length.
        for index, char_a in enumerate(list_of_chars_box_a):
            if char_a != list_of_chars_box_b[index]:
                diff_positions.append(index)

        return diff_positions

    @staticmethod
    def _clean_box_id(box_a, positions_to_remove):
        d_a = list(box_a)

        # remove all the chars at the positions in the list
        for position in positions_to_remove:
            d_a.pop(position)

        return ''.join(d_a)


class Day2(Day):
    """
    Day2 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day2, self).__init__(day_number=2)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day2Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day2Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day2.day {}>".format(self.day_number)

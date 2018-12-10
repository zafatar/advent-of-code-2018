# src/Days/Day3.py

from src.Day import Day
from src.Puzzle import Puzzle

import re


class Claim:
    """Claim class"""
    def __init__(self, claim_line):
        """
        Class constructor reading one line of claim and builds the Claim object.
        :param claim_line:
        """
        claim_match = re.match(r"#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)", claim_line)

        if claim_match.group(0) is not None:
            self.id = int(claim_match.group(1))
            self.distance_to_left = int(claim_match.group(2))
            self.distance_to_top = int(claim_match.group(3))
            self.width = int(claim_match.group(4))
            self.height = int(claim_match.group(5))

    def __repr__(self):
        return "#{} @ {},{}: {}x{}".format(self.id, self.distance_to_left, self.distance_to_top,
                                           self.width, self.height)


class Day3Puzzle1(Puzzle):
    """
    Day3 Puzzle1 class
    """
    def solve(self):
        print("Day3 - Puzzle1")
        claim_lines = self.input.splitlines()

        claimed_coordinates = {}            # keep the claimed coordinates as coordinate => number of claim
        number_of_multiple_claim = 0        # counter for the coordinates claimed multiple times, at least 2.

        for claim_line in claim_lines:
            claim = Claim(claim_line)

            # for each claim, loop all claimed coordinates and increase the claim counter for the coordinate.
            for x in range(claim.distance_to_left, claim.distance_to_left + claim.width):
                for y in range(claim.distance_to_top, claim.distance_to_top + claim.height):
                    coordinate = "{} x {}".format(x, y)
                    if coordinate in claimed_coordinates:
                        claimed_coordinates[coordinate] += 1

                        # increase when a coordinate has a multiple claim, count only when it's 2.
                        if claimed_coordinates[coordinate] == 2:
                            number_of_multiple_claim += 1
                    else:
                        claimed_coordinates[coordinate] = 1

        print("Solution: {}".format(str(number_of_multiple_claim)))


class Day3Puzzle2(Puzzle):
    """
    Day3 Puzzle2 class
    """
    def solve(self):
        print("Day3 - Puzzle2")
        claim_lines = self.input.splitlines()

        claimed_coordinates = {}            # keep the claimed coordinates as coordinate => list of claim ids
        unoverlapped_claims = []            # keep the list of unoverlapped claims.

        for claim_line in claim_lines:
            claim = Claim(claim_line)

            unoverlapped_claims.append(claim.id)   # every claim is un-overlapping until proven overlapping

            # for each claim, loop all claimed coordinates and add the claim id to the coordinate's claim list.
            for x in range(claim.distance_to_left, claim.distance_to_left + claim.width):
                for y in range(claim.distance_to_top, claim.distance_to_top + claim.height):

                    coordinate = "{} x {}".format(x, y)
                    if coordinate not in claimed_coordinates:
                        claimed_coordinates[coordinate] = []

                    claimed_coordinates[coordinate].append(claim.id)

                    # coordinate is claimed by more than 2 claim then we need to check coordinate's claim list
                    if len(claimed_coordinates[coordinate]) >= 2:
                        # this claim is overlapping another claim.
                        for overlapping_claim_id in claimed_coordinates[coordinate]:
                            if overlapping_claim_id in unoverlapped_claims:
                                # remove overlapping claim if it's still in the unoverlapped list.
                                unoverlapped_claims.remove(overlapping_claim_id)

        single_square = unoverlapped_claims[0]
        print("Solution: {}".format(str(single_square)))


class Day3(Day):
    """
    Day1 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day3, self).__init__(day_number=3)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day3Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day3Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day3.day {}>".format(self.day_number)

# src/Days/Day1.py

from src.Day import Day
from src.Puzzle import Puzzle

from datetime import datetime
import re


class Guard:
    """Guard class"""
    def __init__(self, guard_id=0):
        self.id = guard_id
        self.total_sleep_time = 0
        self.sleeping_minutes = {}

    def __repr__(self):
        return "<Guard.id {}>".format(self.id)


class Log:
    """Log class"""
    def __init__(self, log_line=None, guard_id=None):
        log_match = re.match(r"\[(.*?)\] (.*?)$", log_line)
        log_datetime = datetime.strptime(log_match.group(1), '%Y-%m-%d %H:%M')
        log_detail = log_match.group(2)

        if log_detail.startswith("Guard"):
            guard_match = re.match(r"Guard #(\d+)", log_detail)
            guard_id = guard_match.group(1)

        self.datetime = log_datetime
        self.detail = log_detail
        self.guard_id = guard_id


class Day4Puzzle1(Puzzle):
    """
    Day1 Puzzle1 class
    """
    def solve(self):
        print("Day4 - Puzzle1")
        log_lines = self.input.splitlines()

        guards = {}                             # keep the sleeping records for each guard
        guard_sleeping_most = None              # keep track of the guard sleeping most
        guard_on_duty = None                    # guard on duty at the moment
        sleep_starting = None                   # sleep starting time for the guard on duty

        for log_line in sorted(log_lines):      # sort the log lines before analysing them
            log = Log(log_line=log_line)

            if log.detail.startswith("Guard"):
                guard_on_duty = Guard(guard_id=log.guard_id)

            elif log.detail == "falls asleep":
                sleep_starting = log.datetime

            elif log.detail == "wakes up":
                sleep_ending = log.datetime

                # count the sleeping minutes in this shift
                sleep_time_in_mins = int((sleep_ending - sleep_starting).total_seconds() / 60.0)

                # add the sleeping minutes to the sleep time of the guard in duty
                # if not appeared yet, initialize the guard
                if guard_on_duty.id in guards:
                    guards[guard_on_duty.id].total_sleep_time += sleep_time_in_mins
                else:
                    guards[guard_on_duty.id] = guard_on_duty
                    guards[guard_on_duty.id].total_sleep_time = sleep_time_in_mins

                if guard_sleeping_most is None or \
                        guards[guard_on_duty.id].total_sleep_time > guard_sleeping_most.total_sleep_time:
                    guard_sleeping_most = guards[guard_on_duty.id]

                for minute in range(sleep_starting.minute, sleep_ending.minute):
                    if minute in guards[guard_on_duty.id].sleeping_minutes:
                        guards[guard_on_duty.id].sleeping_minutes[minute] += 1
                    else:
                        guards[guard_on_duty.id].sleeping_minutes[minute] = 1

        # analyse the sleeping minutes of the guard sleeping most.
        minute_slept_more = 0
        max_minute_count = 0
        for minute, minute_count in guard_sleeping_most.sleeping_minutes.items():
            if minute_count >= max_minute_count:
                max_minute_count = minute_count
                minute_slept_more = minute

        # the ID of the guard you chose multiplied by the minute you chose?
        coefficient = int(guard_sleeping_most.id) * int(minute_slept_more)

        print("Solution: {}".format(str(coefficient)))


class Day4Puzzle2(Puzzle):
    """
    Day4 Puzzle2 class
    """
    def solve(self):
        print("Day4 - Puzzle2")
        log_lines = self.input.splitlines()

        guards = {}                             # keep the sleeping time for each guard
        guard_sleeping_most_on_a_minute = None  # This time, the guard sleeping most on a specific minute
        max_sleeping_times_on_a_minute = 0      # The minute in which one of the guards slept more
        guard_on_duty = None                    # guard on duty at the moment
        sleep_starting = None                   # sleep starting time for the guard on duty

        for log_line in sorted(log_lines):      # sort the log lines before analysing them
            log = Log(log_line=log_line)

            if log.detail.startswith("Guard"):
                guard_on_duty = Guard(guard_id=log.guard_id)

            elif log.detail == "falls asleep":
                sleep_starting = log.datetime

            elif log.detail == "wakes up":
                sleep_ending = log.datetime

                for minute in range(sleep_starting.minute, sleep_ending.minute):
                    if guard_on_duty.id not in guards:
                        guards[guard_on_duty.id] = guard_on_duty

                    if minute in guards[guard_on_duty.id].sleeping_minutes:
                        guards[guard_on_duty.id].sleeping_minutes[minute] += 1
                    else:
                        guards[guard_on_duty.id].sleeping_minutes[minute] = 1

                    if guards[guard_on_duty.id].sleeping_minutes[minute] >= max_sleeping_times_on_a_minute:
                        max_sleeping_times_on_a_minute = guards[guard_on_duty.id].sleeping_minutes[minute]
                        guard_sleeping_most_on_a_minute = guards[guard_on_duty.id]

        # analyse the sleeping minutes of the guard who slept most on a given minute.
        minute_slept_most = 0
        max_count_on_a_minute = 0
        for minute, count in guard_sleeping_most_on_a_minute.sleeping_minutes.items():
            if count > max_count_on_a_minute:
                max_count_on_a_minute = count
                minute_slept_most = minute

        # the ID of the guard you chose multiplied by the minute you chose?
        coefficient = int(guard_sleeping_most_on_a_minute.id) * int(minute_slept_most)

        print("Solution: {}".format(str(coefficient)))


class Day4(Day):
    """
    Day4 Class with 2 puzzles.
    """
    def __init__(self):
        super(Day4, self).__init__(day_number=4)

    def puzzle(self, puzzle_number=0):
        """
        This method returns the puzzle instance

        :param puzzle_number: number of the puzzle
        :return: instance of the puzzle with the given number of puzzle.
        """
        puzzles_for_day = [
            Day4Puzzle1(puzzle_number=puzzle_number, day_number=self.day_number),
            Day4Puzzle2(puzzle_number=puzzle_number, day_number=self.day_number)
        ]

        return puzzles_for_day[puzzle_number-1]

    def __repr__(self):
        return "<Day4.day {}>".format(self.day_number)

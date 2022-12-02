# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022


def read_lines(input_path: str) -> list[str]:
    with open(input_path) as f:
        return f.readlines()


def read_split(input_path: str, separator: str = "\n") -> list[str]:
    with open(input_path) as f:
        return f.read().split(separator)

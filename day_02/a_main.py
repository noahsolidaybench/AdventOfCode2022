# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)


ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6

match_results = []

for match in input_data:
    mine = match[2]
    opponent = match[0]
    result = 0
    if mine == "X":  # rock
        result += ROCK
        if opponent == "A":  # rock
            result += DRAW
        elif opponent == "B":  # paper
            result += LOSS
        elif opponent == "C":  # scissors
            result += WIN
    elif mine == "Y":  # paper
        result += PAPER
        if opponent == "A":  # rock
            result += WIN
        elif opponent == "B":  # paper
            result += DRAW
        elif opponent == "C":  # scissors
            result += LOSS
    elif mine == "Z":  # scissors
        result += SCISSORS
        if opponent == "A":  # rock
            result += LOSS
        elif opponent == "B":  # paper
            result += WIN
        elif opponent == "C":  # scissors
            result += DRAW

    match_results.append(result)


print(sum(match_results))

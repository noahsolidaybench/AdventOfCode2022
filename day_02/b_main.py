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
    if mine == "X":  # lose
        result += LOSS
        if opponent == "A":  # rock
            result += SCISSORS
        elif opponent == "B":  # paper
            result += ROCK
        elif opponent == "C":  # scissors
            result += PAPER
    elif mine == "Y":  # draw
        result += DRAW
        if opponent == "A":  # rock
            result += ROCK
        elif opponent == "B":  # paper
            result += PAPER
        elif opponent == "C":  # scissors
            result += SCISSORS
    elif mine == "Z":  # win
        result += WIN
        if opponent == "A":  # rock
            result += PAPER
        elif opponent == "B":  # paper
            result += SCISSORS
        elif opponent == "C":  # scissors
            result += ROCK

    match_results.append(result)


print(sum(match_results))

# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils, math_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
#data_path = os.path.join(script_path, "sample_input.txt")
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)

NUM_KNOTS = 10
directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
knots = [(0, 0)] * NUM_KNOTS
unique_pos = {(0, 0)}


for move in input_data:
    direction_raw, count = move.split()
    direction = directions[direction_raw]
    for i in range(int(count)):
        # move head first
        knots[0] = math_utils.add_tuple(knots[0], direction)
        # now move the tails
        for k in range(1, len(knots)):
            tail_direction = math_utils.subtract_tuple(knots[k - 1], knots[k])
            if abs(tail_direction[0]) > 1 or abs(tail_direction[1]) > 1:
                knots[k] = math_utils.add_tuple(knots[k], math_utils.clamp_tuple(tail_direction, -1, 1))

        # log position of last knot
        unique_pos.add(knots[-1])


print(knots[0])
print(knots[-1])
print(len(unique_pos))

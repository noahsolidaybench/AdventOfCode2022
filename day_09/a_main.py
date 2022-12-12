# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils, math_utils

import operator

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
#data_path = os.path.join(script_path, "sample_input.txt")
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)

directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
head_pos = (0, 0)
tail_pos = (0, 0)
unique_pos = set([tail_pos])


for move in input_data:
    direction_raw, count = move.split()
    direction = directions[direction_raw]
    for i in range(int(count)):
        head_pos = math_utils.add_tuple(head_pos, direction)
        tail_direction = math_utils.subtract_tuple(head_pos, tail_pos)
        if abs(tail_direction[0]) > 1 or abs(tail_direction[1]) > 1:
            tail_pos = math_utils.add_tuple(tail_pos, math_utils.clamp_tuple(tail_direction, -1, 1))
            unique_pos.add(tail_pos)


print(head_pos)
print(tail_pos)
print(len(unique_pos))

# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path, "\n\n")


start_config = input_data[0].split("\n")
instructions = input_data[1].split("\n")
containers = {}

# rotate our starting config so we can more easily make each column a list
# stolen from stack overflow
rotated = list(zip(*start_config[::-1]))
for column in rotated:
    if column[0].isdigit():
        # convert to list so we're mutable
        column = list(column)
        # remove any empty spots
        while ' ' in column:
            column.remove(' ')

        # finally add our column to the dict
        containers[column[0]] = column[1:]


for instruction in instructions:
    split_i = instruction.split()
    count = int(split_i[1])
    origin = split_i[3]
    destination = split_i[5]
    for i in range(0, count):
        containers[destination].append(containers[origin].pop())


print(''.join([column[-1] for column in containers.values()]))

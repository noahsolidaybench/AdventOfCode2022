# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
#data_path = os.path.join(script_path, "sample_input.txt")
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)


output = ""
x_val = 1
cycle = 0


def draw_pixel():
    result = ""
    # go to next line if we've hit 40
    if (cycle - 1) % 40 == 0:
        result += "\n"

    if cycle % 40 - 1 in range(x_val - 1, x_val + 2):
        result += "#"

    else:
        result += "."

    return result


for signal in input_data:
    if "noop" in signal:
        cycle += 1
        output += draw_pixel()
        continue

    else:
        for i in range(2):
            cycle += 1
            output += draw_pixel()

        x_val += int(signal.split()[-1])


print(output)

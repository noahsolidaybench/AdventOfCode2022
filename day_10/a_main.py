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


measure_points = [20, 60, 100, 140, 180, 220]
signal_strengths = []
x_val = 1
cycle = 0

for signal in input_data:
    if "noop" in signal:
        cycle += 1
        # check for measurement
        if cycle in measure_points:
            signal_strengths.append(cycle * x_val)
        continue

    else:
        for i in range(2):
            cycle += 1
            # check for measurement
            if cycle in measure_points:
                signal_strengths.append(cycle * x_val)

        x_val += int(signal.split()[-1])


print(sum(signal_strengths))

# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)[0]

signal_start = 0

for i in range(14, len(input_data)):
    last_fourteen = set(input_data[i-14:i])
    if len(last_fourteen) == 14:
        signal_start = i
        break


print(signal_start)

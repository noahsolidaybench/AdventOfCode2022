# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)[0]

signal_start = 0

for i in range(4, len(input_data)):
    last_four = set(input_data[i-4:i])
    if len(last_four) == 4:
        signal_start = i
        break


print(signal_start)

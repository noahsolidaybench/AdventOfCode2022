# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path, "\n\n")

current_elf_calories: int = 0
all_calorie_values: list = []

for elf in input_data:
    all_calorie_values.append(sum([int(c) for c in elf.split()]))

all_calorie_values.sort(reverse=True)

print(sum(all_calorie_values[0:3]))

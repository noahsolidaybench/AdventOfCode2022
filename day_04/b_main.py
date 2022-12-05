# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)


fully_contained_count = 0

for pair in input_data:
    elf_a = set(range(int(pair.split(',')[0].split('-')[0]), int(pair.split(',')[0].split('-')[1]) + 1))
    elf_b = set(range(int(pair.split(',')[1].split('-')[0]), int(pair.split(',')[1].split('-')[1]) + 1))

    if len(elf_a.intersection(elf_b)) > 0:
        fully_contained_count += 1


print(fully_contained_count)

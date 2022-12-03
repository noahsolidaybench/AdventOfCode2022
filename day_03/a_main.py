# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_lines(data_path)

# no 0 priority so just add some bad data to index 0
PRIORITY = ['-', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

misplaced_items = []


def compare_compartments(a, b):
    for item_a in comp_a:
        for item_b in comp_b:
            if item_b == item_a:
                return item_a


for rucksack in input_data:
    comp_a = rucksack[:len(rucksack)//2]
    comp_b = rucksack[len(rucksack)//2:]

    misplaced_items.append(compare_compartments(comp_a, comp_b))


print(sum([PRIORITY.index(item) for item in misplaced_items]))

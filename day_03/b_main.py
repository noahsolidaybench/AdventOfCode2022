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


def compare_compartments(a, b, c):
    for item_a in a:
        for item_b in b:
            for item_c in c:
                if item_b == item_a == item_c:
                    return item_a


for i in range(0, len(input_data), 3):
    misplaced_items.append(compare_compartments(input_data[i], input_data[i+1], input_data[i+2]))


print(sum([PRIORITY.index(item) for item in misplaced_items]))

# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_lines(data_path)


current_elf_calories: int = 0
highest_calorie_value: int = 0

for snack in input_data:
    if snack == '\n':
        if current_elf_calories > highest_calorie_value:
            highest_calorie_value = current_elf_calories

        current_elf_calories = 0
        continue

    current_elf_calories += int(snack)

print(highest_calorie_value)

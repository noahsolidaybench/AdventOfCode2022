# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
#data_path = os.path.join(script_path, "sample_input.txt")
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)

rows = input_data
columns = list(zip(*rows[::-1]))
highest_scenic_score = 0


def get_scenic_score(tree_row_index: int, tree_column_index: int) -> int:
    # early out for trees on the edges, they're garbage town
    if tree_row_index == 0 or \
            tree_column_index == 0 or \
            tree_row_index == len(rows) - 1 or \
            tree_column_index == len(columns) - 1:
        return 0

    tree_height = int(rows[tree_row_index][tree_column_index])

    # begin at the max value and come down
    score_n = tree_row_index
    score_s = len(rows) - tree_row_index - 1
    score_w = tree_column_index
    score_e = len(columns) - tree_column_index - 1

    # reverse some of our tree lists because we need to go outward from the tree's perspective
    trees_to_the_west = reversed(rows[tree_row_index][0:tree_column_index])
    trees_to_the_east = rows[tree_row_index][tree_column_index + 1:]
    trees_to_the_north = columns[tree_column_index][len(rows) - tree_row_index:]
    trees_to_the_south = reversed(columns[tree_column_index][0:len(rows) - tree_row_index - 1])
    for i, tree in enumerate(trees_to_the_west):
        if tree_height <= int(tree):
            score_w = i + 1
            break

    for i, tree in enumerate(trees_to_the_east):
        if tree_height <= int(tree):
            score_e = i + 1
            break

    for i, tree in enumerate(trees_to_the_north):
        if tree_height <= int(tree):
            score_n = i + 1
            break

    for i, tree in enumerate(trees_to_the_south):
        if tree_height <= int(tree):
            score_s = i + 1
            break

    return score_w * score_e * score_n * score_s


for r in range(len(rows)):
    for c in range(len(columns)):
        scenic_score = get_scenic_score(r, c)
        if scenic_score > highest_scenic_score:
            highest_scenic_score = scenic_score


print(highest_scenic_score)

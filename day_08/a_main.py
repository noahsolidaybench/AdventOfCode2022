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
visible_trees = 0


def is_tree_visible(tree_row_index: int, tree_column_index: int) -> bool:
    # early out for trees on the edges
    if tree_row_index == 0 or \
            tree_column_index == 0 or \
            tree_row_index == len(rows) or \
            tree_column_index == len(columns):
        return True

    tree_height = int(rows[tree_row_index][tree_column_index])
    
    tree_vis_n = True
    tree_vis_s = True
    tree_vis_w = True
    tree_vis_e = True

    trees_to_the_west = rows[tree_row_index][0:tree_column_index]
    trees_to_the_east = rows[tree_row_index][tree_column_index + 1:]
    trees_to_the_north = columns[tree_column_index][len(rows) - tree_row_index:]
    trees_to_the_south = columns[tree_column_index][0:len(rows) - tree_row_index - 1]
    for tree in trees_to_the_west:
        if tree_height <= int(tree):
            tree_vis_w = False

    for tree in trees_to_the_east:
        if tree_height <= int(tree):
            tree_vis_e = False

    for tree in trees_to_the_north:
        if tree_height <= int(tree):
            tree_vis_n = False

    for tree in trees_to_the_south:
        if tree_height <= int(tree):
            tree_vis_s = False

    return tree_vis_n or tree_vis_s or tree_vis_w or tree_vis_e


for r in range(len(rows)):
    for c in range(len(columns)):
        if is_tree_visible(r, c):
            visible_trees += 1


print(visible_trees)

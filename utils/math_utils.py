# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import operator


def clamp(num, min_value, max_value):
    """Clamps a number between the given min and max values"""
    return max(min(num, max_value), min_value)


def clamp_tuple(tup: tuple, min_value, max_value) -> tuple:
    """Clamps the values in a tuple between the given min and max values"""
    to_list = list(tup)
    for i in range(len(to_list)):
        to_list[i] = clamp(to_list[i], min_value, max_value)

    return tuple(to_list)


def add_tuple(tuple_a: tuple, tuple_b: tuple) -> tuple:
    """Adds two tuples together"""
    return tuple(map(sum, zip(tuple_a, tuple_b)))


def subtract_tuple(tuple_a: tuple, tuple_b: tuple) -> tuple:
    """Subtracts one tuple from another"""
    return tuple(map(operator.sub, tuple_a, tuple_b))

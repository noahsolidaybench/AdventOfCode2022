# Copyright 2022 Noah Soliday Bench
# Made for Advent of Code 2022

import os
from utils import input_utils

import operator, math

# get our input
script_path = os.path.dirname(os.path.abspath(__file__))
#data_path = os.path.join(script_path, "sample_input.txt")
data_path = os.path.join(script_path, "input.txt")
input_data = input_utils.read_split(data_path)


# stolen from chris marsh
def mult_mod(a):
    x = 1
    for n in a:
        x *= n
    return x


ops = {"+": operator.add, "*": operator.mul}
monkeys = []

# parse our monkey data
current_monkey = -1
for i in range(0, len(input_data), 7):
    current_monkey += 1
    monkey_data = {
        "items": [int(x) for x in input_data[i + 1].split("items: ")[-1].split(",")],
        "op": input_data[i + 2].rsplit(maxsplit=2)[-2:],
        "test": int(input_data[i + 3].rsplit(maxsplit=1)[-1]),
        "true": int(input_data[i + 4].rsplit(maxsplit=1)[-1]),
        "false": int(input_data[i + 5].rsplit(maxsplit=1)[-1]),
        "count": 0}
    monkeys.append(monkey_data)

# multiply all our divisors together. method stolen from chris marsh
mod = mult_mod([m["test"] for m in monkeys])

# run the sequence
for i in range(10000):
    for monkey in monkeys:
        for item in monkey["items"]:
            monkey["count"] += 1
            if monkey["op"][1].isdigit():
                item = ops[monkey["op"][0]](item, int(monkey["op"][1]))
            else:
                # handle "old" case
                item = ops[monkey["op"][0]](item, item)

            item %= mod
            target = monkey["true"] if item % monkey["test"] == 0 else monkey["false"]
            monkeys[target]["items"].append(item)

        monkey["items"].clear()

# sort em and multiply em
monkeys = sorted(monkeys, key=lambda x: x["count"], reverse=False)
print(operator.mul(*(x["count"] for x in monkeys[-2:])))

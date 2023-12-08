import re
import numpy as np

directions = ""
values = {}

with open("input.txt") as file:
    for index, line in enumerate(file.readlines()):
        line = line.strip()

        if index == 0:
            directions = line
            continue
        
        if index == 1:
            continue

        values[line[0:3]] = [line[7:10], line[12:15]]

keys = []

for value in values.keys():
    if value[-1] == "A":
        keys.append(value)

first_found = [0]*len(keys)

count = 0
pos = 0
next_round = True

while next_round:
    for index, key in enumerate(keys):
        if directions[pos] == "L":
            keys[index] = values[key][0]

        if directions[pos] == "R":
            keys[index] = values[key][1]

    count += 1
    pos += 1

    if pos == len(directions):
        pos = 0

    for index, key in enumerate(keys):
        if key[-1] == "Z":
            first_found[index] = count

    next_round = False
    for found in first_found:
        if found == 0:
            next_round = True
            break

print(np.lcm.reduce(first_found))
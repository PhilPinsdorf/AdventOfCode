import re

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

key = "AAA"
count = 0
index = 0

while key != "ZZZ":
    if directions[index] == "L":
        key = values[key][0]

    if directions[index] == "R":
        key = values[key][1]

    count += 1
    index += 1

    if index == len(directions):
        index = 0

print(count)

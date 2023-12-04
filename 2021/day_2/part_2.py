import re

f = open('input.txt', 'r')
txt = f.read()

pattern = re.compile(r"forward ([1-9]+)|up ([1-9]+)|down ([1-9])")
match = re.findall(pattern, txt)

aim = 0
horizontal = 0
depth = 0

for entry in match:
    if(entry[0] != ''):
        horizontal += int(entry[0])
        depth += int(entry[0]) * aim

    if(entry[1] != ''):
        aim -= int(entry[1])

    if(entry[2] != ''):
        aim += int(entry[2])

print(horizontal * depth)

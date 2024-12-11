import re

count_1, count_2 = 0, 0
f = open("input.txt", "r")

def part_1(line):
    if len(re.findall(r'([aeiou])', line)) < 3:
        return
    if len(re.findall(r'(.)\1+', line)) < 1:
        return
    if len(re.findall(r'(ab|cd|pq|xy)', line)) > 0:
        return
    count_1 += 1

def part_2(line):
    if len(re.findall(r'(([a-z]{2}).*?\1)', line)) < 1:
        return
    if len(re.findall(r'([a-z]).\1', line)) < 1:
        return
    count_2 += 1

for line in f.readlines():
    part_1(line)
    part_2(line)
    
print(count_1)
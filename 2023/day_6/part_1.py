import re
import math

score = 1
times = []
distances = []

with open("input.txt") as file:
    lines = file.readlines()
    times = [int(a) for a in re.findall("\d+", lines[0].strip())]
    distances = [int(a) for a in re.findall("\d+", lines[1].strip())]

for i in range(4):
    min = math.ceil((times[i] / 2) - math.sqrt((-times[i] / 2)**2 - distances[i] - 1))
    max = math.floor((times[i] / 2) + math.sqrt((-times[i] / 2)**2 - distances[i] - 1))

    score *= max - min + 1
    
print(score)
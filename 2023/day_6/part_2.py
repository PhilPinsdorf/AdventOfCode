import re
import math

time = 0
distance = 0

with open("input.txt") as file:
    lines = file.readlines()
    time = int(re.findall("\d+", lines[0].strip().replace(" ", ""))[0])
    distance = int(re.findall("\d+", lines[1].strip().replace(" ", ""))[0])

min = math.ceil((time / 2) - math.sqrt((-time / 2)**2 - distance - 1))
max = math.floor((time / 2) + math.sqrt((-time / 2)**2 - distance - 1))
    
print(max - min + 1)
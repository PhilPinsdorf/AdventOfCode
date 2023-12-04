import re

input = []
score = 0

with open("input.txt") as file:
    for line in file.readlines():
        input.append(line.strip())

for index, line in enumerate(input):
    for m in re.finditer(r'[0-9]+', line):
        searchstring = ""

        start_x = max(0, min(m.start(0) - 1, len(line) - 1)) 
        end_x = max(0, min(m.end(0), len(line) - 1))  # - 1 + 1 = 0
        start_y = max(0, min(index - 1, len(input) - 1))
        end_y = max(0, min(index + 1, len(input) - 1))

        for i in range(start_y, end_y + 1):
            searchstring += input[i][start_x:end_x + 1]
        
        result = re.sub(r'[0-9]|\.',  '', searchstring)
        
        if len(result) > 0:
            score += int(line[m.start(0):m.end(0)])

print(score)
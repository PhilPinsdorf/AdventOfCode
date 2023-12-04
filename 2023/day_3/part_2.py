import re

input = []
score = 0

with open("input.txt") as file:
    for line in file.readlines():
        input.append(line.strip())

for index, line in enumerate(input):
    for m in re.finditer(r'\*', line):
        searchstring = ""

        start_x = max(0, min(m.start(0) - 3, len(line) - 1))
        end_x = max(0, min(m.end(0) + 2, len(line) - 1))
        start_y = max(0, min(index - 1, len(input) - 1))
        end_y = max(0, min(index + 1, len(input) - 1))

        for i in range(start_y, end_y + 1):
            possible = input[i][start_x:end_x + 1]

            if possible[2] == '.':
                possible = "..." + possible[3:]
            
            if possible[4] == '.':
                possible = possible[:-3] + "..."

            if possible[1] == '.':
                possible = ".." + possible[2:]
            
            if possible[5] == '.':
                possible = possible[:-2] + ".."

            searchstring += possible + '.'

        result = re.sub(r'[^0-9]',  '.', searchstring)

        numbers = []
        for n in re.findall(r'[0-9]+', result):
            numbers.append(int(n))

        if len(numbers) == 2:
            score += numbers[0] * numbers[1]

print(score)
score = 0

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        winning_numbers = set(line[10:39].replace('  ', ' ').split())
        drawn_numbers = set(line[42:].replace('  ', ' ').split())

        score += (0b0000000000000001 << len(winning_numbers & drawn_numbers)) >> 1

print(score)
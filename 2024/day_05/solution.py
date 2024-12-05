from collections import defaultdict
number_dict = defaultdict(list)
count_1, count_2 = 0, 0

f = open("input.txt", "r")
for line in f:
    if line == '\n': break
    sequence = list(map(int, line.split('|')))
    number_dict[sequence[0]].append(sequence[1])

for line in f:
    marked = False
    sequence = list(map(int, line.split(',')))
    while True:
        for index in range(len(sequence) - 1):
            if sequence[index + 1] not in number_dict[sequence[index]]:
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
                marked = True
                break
        else:
            count = sequence[len(sequence) // 2] # Simplifyed Version of math.floor(len(sequence) / 2) 
            if not marked:  count_1 += count
            else:           count_2 += count
            break

print(count_1, count_2)
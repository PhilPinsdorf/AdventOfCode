sequences = []
count_1, count_2, counter = 0, 0, 0

f = open("input.txt", "r")
for line in f:
    parts = line.split(':')
    sequences.append((int(parts[0]), list(map(int, parts[1].split()))))

def find_solutions_recursive(current, sequence, position, solutions, combine):
    if(position == len(sequence)):
        solutions.add(current)
        return

    find_solutions_recursive(current + sequence[position], sequence, position + 1, solutions, combine)
    find_solutions_recursive(current * sequence[position], sequence, position + 1, solutions, combine)
    if combine: find_solutions_recursive(int(str(current) + str(sequence[position])), sequence, position + 1, solutions, combine)

for sequence in sequences: 
    solutions_1, solutions_2, found_1, found_2 = set(), set(), 0, 0
    find_solutions_recursive(sequence[1][0], sequence[1], 1, solutions_1, False)
    find_solutions_recursive(sequence[1][0], sequence[1], 1, solutions_2, True)
    
    if sequence[0] in solutions_1: count_1 += sequence[0]
    if sequence[0] in solutions_2: count_2 += sequence[0]
    
    counter += 1
    print(counter)

print(count_1, count_2)
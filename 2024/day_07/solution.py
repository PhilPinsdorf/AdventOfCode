sequences = []
count_1, count_2 = 0, 0

f = open("input.txt", "r")
for line in f:
    parts = line.split(':')
    sequences.append((int(parts[0]), list(map(int, parts[1].split()))))

def find_solutions_recursive(current, sequence, position, solutions):
    if(position == len(sequence)):
        solutions.add(current)
        return

    find_solutions_recursive(current + sequence[position], sequence, position + 1, solutions)
    find_solutions_recursive(current * sequence[position], sequence, position + 1, solutions)

def build_new_sequences(new_sequence, position, new_sequences):
    if(position >= len(new_sequence) - 1):
        new_sequences.add(tuple(new_sequence))
        return

    # skip one index
    build_new_sequences(new_sequence.copy(), position + 1, new_sequences)
    
    # join two indexes
    adjusted_sequence = new_sequence.copy()
    adjusted_sequence[position] = int(str(adjusted_sequence[position]) + str(adjusted_sequence[position + 1]))
    del adjusted_sequence[position + 1]
    build_new_sequences(adjusted_sequence, position + 1, new_sequences)
    build_new_sequences(adjusted_sequence, 0, new_sequences)

counter, lol = 0, 0
for sequence in sequences:
    solutions_1, solutions_2 = set(), set()
    find_solutions_recursive(sequence[1][0], sequence[1], 1, solutions_1)
    
    new_sequences = set()
    build_new_sequences(sequence[1].copy(), 0, new_sequences)
    new_sequences = [list(elem) for elem in new_sequences]
    
    for new_sequence in new_sequences:
        find_solutions_recursive(new_sequence[0], new_sequence, 1, solutions_2)
        # print(sequence[0], solutions_2)
        if sequence[0] in solutions_2:
            count_2 += sequence[0]
            counter += 1
            break;
    
    if sequence[0] in solutions_1:
        count_1 += sequence[0]
    
    lol += 1
    print(lol, 850)

print(count_1, count_2, counter)
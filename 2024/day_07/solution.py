import multiprocessing

sequences = []
count_1, count_2, iter_count = 0, 0, 0

f = open("input.txt", "r")
for line in f:
    parts = line.split(':')
    sequences.append((int(parts[0]), list(map(int, parts[1].split()))))

def find_solutions_recursive_1(current, sequence, position, solutions):
    if(position == len(sequence)):
        solutions.add(current)
        return

    find_solutions_recursive_1(current + sequence[position], sequence, position + 1, solutions)
    find_solutions_recursive_1(current * sequence[position], sequence, position + 1, solutions)

def find_solutions_recursive_2(current, sequence, position, solutions):
    if(position == len(sequence)):
        solutions.add(current)
        return

    find_solutions_recursive_2(current + ' + ' + str(sequence[position]), sequence, position + 1, solutions)
    find_solutions_recursive_2(current + ' * ' + str(sequence[position]), sequence, position + 1, solutions)
    find_solutions_recursive_2(current + ' | ' + str(sequence[position]), sequence, position + 1, solutions)

def interpret_string(string):
    operations = string.split()
    
    while(len(operations) > 1):
        match operations[1]:
            case '+':
                operations[0] = str(int(operations[0]) + int(operations[2]))
            case '*':
                operations[0] = str(int(operations[0]) * int(operations[2]))
            case '|':
                operations[0] = operations[0] + operations[2]
        
        del operations[1]
        del operations[1]
        
    return int(operations[0])

def calculate_result(args):
    sequence, index = args  
    solutions_1, solutions_2 = set(), set()
    found_1, found_2 = 0, 0
    find_solutions_recursive_1(sequence[1][0], sequence[1], 1, solutions_1)
    find_solutions_recursive_2(str(sequence[1][0]), sequence[1], 1, solutions_2)
    
    if sequence[0] in solutions_1:
        found_1 = sequence[0]
    
    for solution in solutions_2:
        result = interpret_string(solution)
        
        if result == sequence[0]:
            found_2 = sequence[0]
            print(index)
            return (found_1, found_2)
    
    return (found_1, found_2)
    
with multiprocessing.Pool() as pool:
    args = [(sequence, index) for index, sequence in enumerate(sequences)]
    results = pool.map(calculate_result, args)
    for found_1, found_2 in results:
        count_1 += found_1
        count_2 += found_2

print(count_1, count_2)
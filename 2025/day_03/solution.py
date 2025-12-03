from aoc_utils import read_input

data = read_input(use_test_file=False)

def solve_1():
    return sum(find_highest_sequence(line, 2) for line in data)

def solve_2():
    return sum(find_highest_sequence(line, 12) for line in data)

def find_highest_sequence(line, count):
    current_pos = 0
    result = []
    
    for remaining in range(count - 1, -1, -1):
        search_end = len(line) - remaining
        window = line[current_pos : search_end]
        best_char = max(window)
        current_pos += window.index(best_char) + 1
        
        result.append(best_char)

    return int("".join(result))
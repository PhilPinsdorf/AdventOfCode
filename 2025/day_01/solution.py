from aoc_utils import read_input

data = read_input(use_test_file=False)

def solve_1():
    solution = 0 
    dial = 50

    directions = {"L": -1, "R": 1}

    for rotation in data:
        direction = rotation[0]
        clicks = int(rotation[1:])
        
        sign = directions[direction]
        dial = (dial + (sign * clicks)) % 100 
        
        if dial == 0:
            solution += 1
            
    return solution

def solve_2():
    return sum(1 for pos in simulate_dial(data) if pos == 0)

def simulate_dial(instructions):
    dial = 50
    directions = {"L": -1, "R": 1}
    
    for rotation in instructions:
        step = directions[rotation[0]]
        clicks = int(rotation[1:])
        
        for _ in range(clicks):
            dial = (dial + step) % 100
            yield dial
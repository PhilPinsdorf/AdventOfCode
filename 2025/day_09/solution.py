from aoc_utils import read_input
import sys

data = read_input(use_test_file=True, separator=',', cast_to=int)

def solve_1():
    solution = 0
    min, max = [sys.maxsize, sys.maxsize], [0, 0]
    min_score, max_score = sys.maxsize * 2, 0
    
    for position in data:
        score = position[0] + position[1]

        if score < min_score:
            min = position
            min_score = score
        
        if score > max_score:
            max = position
            max_score = score
 
    print(min, max)
    return ((max[0] - min[0]) * max[1] - min[1])

def solve_2():
    solution = 0
    return solution
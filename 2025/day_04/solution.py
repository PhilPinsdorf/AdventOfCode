from aoc_utils import read_input

data = read_input(use_test_file=False, cast_to=list)
max_width = len(data[0])
max_height = len(data)

def solve_1():
    accessible = 0
    for index_y, data_y in enumerate(data):
        for index_x, data_x in enumerate(data_y):
            if data_x == '.':
                continue
            
            num_rolls = sum(paperroll_on_pos(index_x + dx, index_y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)
            
            if num_rolls < 4:
                accessible += 1

    return accessible

def solve_2():
    accessible = 0
    next_roud_needed = True

    data_2 = data 

    while (next_roud_needed):
        accessible_this_round = 0
        
        for index_y, _ in enumerate(data_2):
            for index_x, _ in enumerate(data_2[index_y]):
                if data_2[index_y][index_x] == '.':
                    continue
                
                num_rolls = sum(paperroll_on_pos(index_x + dx, index_y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx or dy)
                
                if num_rolls < 4:
                    accessible_this_round += 1
                    data_2[index_y][index_x] = '.'

        accessible += accessible_this_round

        if accessible_this_round == 0:
            next_roud_needed = False

    return accessible

def paperroll_on_pos(x, y):
    if x < 0 or x >= max_width:
        return False
    if y < 0 or y >= max_height:
        return False
    
    if data[y][x] == '@':
        return True
    
    return False

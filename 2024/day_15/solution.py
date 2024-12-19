grid, bigger_grid = [], []
sequence = ""
robot_x_1, robot_y_1 = 0, 0
robot_x_2, robot_y_2 = 0, 0
score_1, score_2 = 0, 0

f = open("input.txt", "r")

for index, line in enumerate(f):
    if line == '\n': break
    
    if '@' in line:
        robot_x_1, robot_y_1 = line.find('@'), index
    grid.append(list(line.strip()))
    
    new_line = ""
    for char in line:
        match char:
            case '#': new_line += '##'
            case 'O': new_line += '[]'
            case '.': new_line += '..'
            case '@': new_line += '@.'
    
    if '@' in new_line:
        robot_x_2, robot_y_2 = new_line.find('@'), index
    bigger_grid.append(list(new_line))
    
for line in f:
    sequence += line.strip()

def move(step_x, step_y):
    global robot_x_1, robot_y_1
    found, char_x, char_y = valid_recursive(robot_x_1, robot_y_1, step_x, step_y)
    if found:
        move_recursive(char_x, char_y, step_x, step_y)
        robot_x_1 += step_x
        robot_y_1 += step_y
    pass

def move_lr(step_x):
    global robot_x_2
    possible, char_x = valid_recursive_lr(robot_x_2, step_x)
    if possible:
        move_recursive_lr(char_x, step_x)
        robot_x_2 += step_x
    pass

def move_ud(step_y):
    global robot_y_2
    possible = valid_recursive_ud(robot_x_2, robot_y_2, step_y)
    if possible:
        move_recursive_ud(robot_x_2, robot_y_2 + step_y, step_y)
        robot_y_2 += step_y
    pass

def move_recursive(pos_x, pos_y, step_x, step_y):
    if pos_x == robot_x_1 and pos_y == robot_y_1:
        grid[pos_y][pos_x] = '.'
        return
    
    grid[pos_y][pos_x] = grid[pos_y - step_y][pos_x - step_x]
    move_recursive(pos_x - step_x, pos_y - step_y, step_x, step_y)
    pass

def move_recursive_lr(pos_x, step_x):
    if pos_x == robot_x_2:
        bigger_grid[robot_y_2][pos_x] = '.'
        return
    
    bigger_grid[robot_y_2][pos_x] = bigger_grid[robot_y_2][pos_x - step_x]
    move_recursive_lr(pos_x - step_x, step_x)
    pass

def move_recursive_ud(pos_x, pos_y, step_y):
    char = bigger_grid[pos_y][pos_x]
    if char != '.':
        if char == '[':
            move_recursive_ud(pos_x, pos_y + step_y, step_y)
            move_recursive_ud(pos_x + 1, pos_y + step_y, step_y)
        elif char == ']':
            move_recursive_ud(pos_x, pos_y + step_y, step_y)
            move_recursive_ud(pos_x - 1, pos_y + step_y, step_y)
    
    bigger_grid[pos_y][pos_x] = bigger_grid[pos_y - step_y][pos_x]
    bigger_grid[pos_y - step_y][pos_x] = '.'
    pass

def valid_recursive(pos_x, pos_y, step_x, step_y):
    char = grid[pos_y + step_y][pos_x + step_x]
    if char == '#': return False, -1, -1
    if char == '.': return True, pos_x + step_x, pos_y + step_y
    return valid_recursive(pos_x + step_x, pos_y + step_y, step_x, step_y)

def valid_recursive_lr(pos_x, step_x):
    char = bigger_grid[robot_y_2][pos_x + step_x]
    if char == '#': return False, -1
    if char == '.': return True, pos_x + step_x
    return valid_recursive_lr(pos_x + step_x, step_x)

def valid_recursive_ud(pos_x, pos_y, step_y):
    char = bigger_grid[pos_y + step_y][pos_x]
    if char == '#': return False
    if char == '.': return True
    
    if char == '[':
        return valid_recursive_ud(pos_x, pos_y + step_y, step_y) and valid_recursive_ud(pos_x + 1, pos_y + step_y, step_y)
    if char == ']':
        return valid_recursive_ud(pos_x, pos_y + step_y, step_y) and valid_recursive_ud(pos_x - 1, pos_y + step_y, step_y)

for step in sequence:
    match step:
        case 'v': 
            move(0, 1)
            move_ud(1)
        case '^': 
            move(0, -1)
            move_ud(-1)
        case '<': 
            move(-1, 0)
            move_lr(-1)
        case '>': 
            move(1, 0)
            move_lr(1)

for index_y, line in enumerate(grid):
    for index_x, char in enumerate(line):
        if char == 'O':
            score_1 += 100*index_y + index_x

for index_y, line in enumerate(bigger_grid):
    for index_x, char in enumerate(line):
        if char == '[':
            score_2 += 100*index_y + index_x

print(score_1, score_2)
grid, visited, possible_positions, found_positions = [], set(), set(), set()
count_1, count_2, pos_y, pos_x, start_y, start_x, rotation = 0, 0, 0, 0, 0, 0, 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

f = open("input.txt", "r")
for index, line in enumerate(f):
    grid.append(list(line.strip()))
    if '^' in line:
        start_y, start_x = index, line.index('^')
        pos_y, pos_x = start_y, start_x

while True:
    visited.add((pos_y, pos_x))
    pos_y_next, pos_x_next = pos_y + directions[rotation][0], pos_x + directions[rotation][1]
    
    if not (0 <= pos_y_next < len(grid) and 0 <= pos_x_next < len(grid[0])):
        break;

    if grid[pos_y_next][pos_x_next] == '#':
        rotation = (rotation + 1) % 4
    else:
        pos_y, pos_x = pos_y_next, pos_x_next
        possible_positions.add((pos_y, pos_x))

possible_positions.remove((start_y, start_x))
for obs_y, obs_x in possible_positions:
    visited_positions = set()
    grid[obs_y][obs_x] = '#'
    rotation, pos_y, pos_x = 0, start_y, start_x
    
    while True:
        if (rotation, pos_y, pos_x) in visited_positions:
            found_positions.add((obs_y, obs_x))
            break;
        
        visited_positions.add((rotation, pos_y, pos_x))
        pos_y_next, pos_x_next = pos_y + directions[rotation][0], pos_x + directions[rotation][1]
        
        if not (0 <= pos_y_next < len(grid) and 0 <= pos_x_next < len(grid[0])):
            break;

        if grid[pos_y_next][pos_x_next] == '#':
            rotation = (rotation + 1) % 4
        else:
            pos_y, pos_x = pos_y_next, pos_x_next
    
    grid[obs_y][obs_x] = '.'

count_1, count_2 = len(visited), len(found_positions) 
print(count_1, count_2)
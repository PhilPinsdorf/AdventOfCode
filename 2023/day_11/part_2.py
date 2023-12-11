from collections import defaultdict

star_map = []
galaxy_pos = []
distances = 0

def length(l):
    value = len(list(filter(lambda x: (x == "*"), l)))*999999
    value += len(list(filter(lambda x: (x != "*"), l)))
    return value 

def difference(list1, list2):
    return abs(length(list2) - length(list1))

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        star_map.append(list(line))

        if len(line.replace('.', '')) == 0:
            star_map.append(list("*"*len(line)))
    
free_positions = defaultdict(int)
for line_index, line in enumerate(star_map):
    for char_index, char in enumerate(line):
        if char in ['.', '*']: 
            free_positions[char_index] += 1

free_positions = {k: v for k, v in free_positions.items() if v == len(star_map)}

for i, key in enumerate(free_positions):
    for index, line in enumerate(star_map):
        line.insert(key + i, '*')

for line_index, line in enumerate(star_map):
    for char_index, char in enumerate(line):
        if char == '#': 
            galaxy_pos.append((char_index, line_index))

for line in star_map:
    print(''.join(line))

for i in range(len(galaxy_pos)):
    for j in range(i, len(galaxy_pos)):
        space_x_i = star_map[galaxy_pos[i][1]][:galaxy_pos[i][0] + 1]
        space_x_j = star_map[galaxy_pos[j][1]][:galaxy_pos[j][0] + 1]
        
        space_y_i = []
        for k in range(galaxy_pos[i][1]):
            space_y_i.append(star_map[k][galaxy_pos[i][0]])

        space_y_j = []
        for k in range(galaxy_pos[j][1]):
            space_y_j.append(star_map[k][galaxy_pos[j][0]])

        distances += difference(space_y_i, space_y_j) + difference(space_x_i, space_x_j)
        
print(distances)
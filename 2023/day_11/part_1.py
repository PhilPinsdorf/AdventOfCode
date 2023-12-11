from collections import defaultdict

star_map = []
galaxy_pos = []
distances = 0

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        star_map.append(list(line))

        if len(line.replace('.', '')) == 0:
            star_map.append(list(line))
    
free_positions = defaultdict(int)
for line_index, line in enumerate(star_map):
    for char_index, char in enumerate(line):
        if char == '.': 
            free_positions[char_index] += 1

free_positions = {k: v for k, v in free_positions.items() if v == len(star_map)}

for i, key in enumerate(free_positions):
    for index, line in enumerate(star_map):
        line.insert(key + i, '.')

for line_index, line in enumerate(star_map):
    for char_index, char in enumerate(line):
        if char == '#': 
            galaxy_pos.append((char_index, line_index))

for line in star_map:
    print(''.join(line))

for i in range(len(galaxy_pos)):
    for j in range(i, len(galaxy_pos)):
        distances += abs(galaxy_pos[j][1] - galaxy_pos[i][1]) + abs(galaxy_pos[j][0] - galaxy_pos[i][0])

print(distances)
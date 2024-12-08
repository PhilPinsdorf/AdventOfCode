from itertools import combinations
antennas, antinodes_1, antinodes_2, bounds_x, bounds_y, count_1, count_2 = {}, set(), set(), 0, 0, 0, 0

f = open("test.txt", "r")
for index_y, line in enumerate(f):
    bounds_x, bounds_y = len(line) - 1, index_y
    for index_x, location in enumerate(line.strip()):
        if location != '.':
            antennas.setdefault(location, []).append((index_x, index_y))

def add_antinode(pos, dif, dir, antinode_set, step_multiplier=1):
    antinode = pos[0] + dif[0] * dir * step_multiplier, pos[1] + dif[1] * dir * step_multiplier
    if 0 <= antinode[0] <= bounds_x and 0 <= antinode[1] <= bounds_y:
        antinode_set.add(antinode)
        return True
    return False

def generate_antinodes(start_pos, dif, dir, antinode_set):
    count = 0
    while add_antinode(start_pos, dif, dir, antinode_set, count):
        count += 1

for antenna, antenna_positions in antennas.items():
    for antenna_pos_1, antenna_pos_2 in combinations(antenna_positions, 2):
        dif = (antenna_pos_2[0] - antenna_pos_1[0], antenna_pos_2[1] - antenna_pos_1[1])

        add_antinode(antenna_pos_1, dif, -1, antinodes_1)
        add_antinode(antenna_pos_2, dif, 1, antinodes_1)

        generate_antinodes(antenna_pos_1, dif, -1, antinodes_2)
        generate_antinodes(antenna_pos_2, dif, 1, antinodes_2)
    
count_1, count_2 = len(antinodes_1), len(antinodes_2)
print(count_1, count_2)
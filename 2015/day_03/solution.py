positions_1, positions_2 = {(0, 0)}, {(0, 0)}  # Set to track visited positions
pos_1   = [0, 0]
pos_2_1 = [0, 0]  # Position for the first character
pos_2_2 = [0, 0]  # Position for the second character

f = open("input.txt", "r")
line = f.readline()

def update_position(position, direction):
    match direction:
        case '<':
            position[0] -= 1
        case '>':
            position[0] += 1
        case '^':
            position[1] += 1
        case 'v':
            position[1] -= 1

for index, char in enumerate(list(line)):
    update_position(pos_1, char)
    positions_1.add(tuple(pos_1))
        
    if index % 2 == 0: 
        update_position(pos_2_1, char)
        positions_2.add(tuple(pos_2_1))
    else: 
        update_position(pos_2_2, char)
        positions_2.add(tuple(pos_2_2))

count_1 = len(positions_1)
count_2 = len(positions_2)
print(count_1, count_2)
from operator import itemgetter

count_1, count_2 = 0, 0
garden = []
garden_positions = set()

f = open("input.txt", "r")
for line in f.readlines():
    garden.append(list(line.strip()))
size_x, size_y = len(garden[0]), len(garden)

def find_recursive(pos_x, pos_y, char, positions):
    global size_x, size_y

    if not (0 <= pos_x < size_x and 0 <= pos_y < size_y): return 1
    if garden[pos_y][pos_x] != char: return 1
    if (pos_x, pos_y) in positions: return 0
    
    positions.add((pos_x, pos_y))
    garden_positions.add((pos_x, pos_y))
    return find_recursive(pos_x + 1, pos_y, char, positions) + find_recursive(pos_x - 1, pos_y, char, positions) + find_recursive(pos_x, pos_y + 1, char, positions) + find_recursive(pos_x, pos_y - 1, char, positions) 

def find_consecutive(nums):
    if not nums:
        return 0
    
    score = 1
    for i in range(1, len(nums)): 
        if nums[i] - nums[i - 1] > 1:
            score += 1
    return score

def scan_one_side(start, stop, direction, wall_check, wall_check_x_y, step_x, step_y, append_x_y, layer_manipulation, positions):
    score = 0
    for curr_layer in range(start, stop, direction):
        full_layer = [tuple for tuple in positions if tuple[wall_check_x_y] == curr_layer + layer_manipulation]
        filtered_indexes = []
        for tuple in full_layer:
            # Outermost Layer
            if tuple[wall_check_x_y] == wall_check:
                filtered_indexes.append(tuple[append_x_y])
                continue

            # Anderer Buchstabe beim zurückblicken
            if garden[tuple[1] + step_y][tuple[0] + step_x] != char:
                filtered_indexes.append(tuple[append_x_y])
                continue
        
        filtered_indexes.sort()
        score += find_consecutive(filtered_indexes)
    return score


def find_sides(positions, char):
    score = 0

    # Top Bottom
    max_x = max(positions, key=itemgetter(0))[0]
    max_y = max(positions, key=itemgetter(1))[1]
    min_x = min(positions, key=itemgetter(0))[0]
    min_y = min(positions, key=itemgetter(1))[1]

    #Scan Block
    score += scan_one_side(min_y, max_y + 1, 1, 0, 1, 0, -1, 0, 0, positions) # Scan Top to Bottom -> Blick back up
    score += scan_one_side(max_y + 1, min_y, -1, max_y, 1, 0, 1, 0, -1, positions) # Scan Bottom to Top -> Blick back down
    score += scan_one_side(min_x, max_x + 1, 1, 0, 0, -1, 0, 1, 0, positions) # Scan Left to Right -> Blick back left
    score += scan_one_side(max_x + 1, min_x, -1, max_x, 0, 1, 0, 1, -1, positions) # Scan Right to Left -> Blick back right

    return score

for index_y, row in enumerate(garden):
    for index_x, char in enumerate(row):
        if (index_x, index_y) not in garden_positions:
            positions = set()
            count_1 += find_recursive(index_x, index_y, char, positions) * len(positions)
            count_2 += find_sides(positions, char) * len(positions)

print(count_1, count_2)
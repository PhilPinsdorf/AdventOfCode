hills = []
count_1, count_2 = 0, 0
f = open("input.txt", "r")
for line in f.readlines():
    hills.append(list(map(int, line.strip())))

def search_recursive(pos_x, pos_y, next_num, positions):
    global count_2
    
    if not (0 <= pos_y < len(hills) and 0 <= pos_x < len(hills[pos_y])):
        return
    if hills[pos_y][pos_x] != next_num:
        return
    if next_num == 9:
        positions.add((pos_x, pos_y))
        count_2 += 1
        return
    
    search_recursive(pos_x + 1, pos_y, next_num + 1, positions)
    search_recursive(pos_x - 1, pos_y, next_num + 1, positions)
    search_recursive(pos_x, pos_y + 1, next_num + 1, positions)
    search_recursive(pos_x, pos_y - 1, next_num + 1, positions)

for i in range(len(hills)):
    for j in range(len(hills[i])):
        if hills[i][j] == 0:
            positions = set()
            search_recursive(j, i, 0, positions)
            count_1 += len(positions)
            
print(count_1, count_2)
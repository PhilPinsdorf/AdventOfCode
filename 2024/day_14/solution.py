import re
from collections import defaultdict
from PIL import Image

robots = defaultdict(list)
size_x, size_y = 101, 103
smallest_seconds, smallest_score, tree_image = 0, 0, Image.new('1', (size_x, size_y))

f = open("input.txt", "r")

for line in f.readlines():
    match = re.findall(r"(-?\d+),(-?\d+)", line)
    match = [tuple(map(int,t)) for t in match]
    robots[match[0]].append(match[1])

def create_image():
    global tree_image
    img = Image.new('1', (size_x, size_y))
    for y in range(size_y):
        for x in range(size_x):
            if (x, y) in robots.keys():
                img.putpixel((x, y), 1)
    
    tree_image = img
    
for second in range(10000):
    robots_copy = robots.copy()
    robots.clear()
   
    for position, robot_list in robots_copy.items():
        for robot in robot_list:
            new_pos = list(map(lambda i, j: i + j, position, robot))
            new_pos[0] %= size_x
            new_pos[1] %= size_y
            robots[tuple(new_pos)].append(robot)
    
    q1 = sum([len(v) for k, v in robots.items() if 0 <= k[0] < size_x // 2 and 0 <= k[1] < size_y // 2])
    q2 = sum([len(v) for k, v in robots.items() if size_x // 2 < k[0] < size_x and 0 <= k[1] < size_y // 2])
    q3 = sum([len(v) for k, v in robots.items() if 0 <= k[0] < size_x // 2 and size_y // 2 < k[1] < size_y])
    q4 = sum([len(v) for k, v in robots.items() if size_x // 2 < k[0] < size_x and size_y // 2 < k[1] < size_y])
    score = q1 * q2 * q3 * q4
    
    if second == 99:
        print("100:", score)
    
    if smallest_score == 0 or score < smallest_score:
        smallest_score = score
        smallest_seconds = second + 1
        create_image()
        print(second + 1)

tree_image.save("pictures/" + str(smallest_score) + "_robots_" + str(smallest_seconds) + ".bmp")
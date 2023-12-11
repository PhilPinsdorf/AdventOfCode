import math

maze = []
steps = 1
pos = [0, 0]
pipes = {"|": [1, 0, 1, 0], "L": [1, 1, 0, 0], "J": [1, 0, 0, 1], "F": [0, 1, 1, 0], "7": [0, 0, 1, 1], "-": [0, 1, 0, 1]}
came_from = [0, 0, 0, 0]

def find_start():    
    global pos, came_from 

    if pipes[maze[pos[1] + 1][pos[0]]][0] == 1:
        pos[1] += 1
        came_from = [1, 0, 0, 0]
        return

    if pipes[maze[pos[1]][pos[0] + 1]][1] == 1:
        pos[0] += 1
        came_from = [0, 1, 0, 0]
        return

    if pipes[maze[pos[1] - 1][pos[0]]][2] == 1:
        pos[1] -= 1
        came_from = [0, 0, 1, 0]
        return

    if pipes[maze[pos[1]][pos[0] - 1]][3] == 1:
        pos[0] -= 1
        came_from = [0, 0, 0, 1]
        return

def take_step():
    global pos, came_from

    if came_from[0] == 0 and pipes[maze[pos[1]][pos[0]]][0] == 1:
        pos[1] -= 1
        came_from = [0, 0, 1, 0]
        return

    if came_from[1] == 0 and pipes[maze[pos[1]][pos[0]]][1] == 1:
        pos[0] += 1
        came_from = [0, 0, 0, 1]
        return

    if came_from[2] == 0 and pipes[maze[pos[1]][pos[0]]][2] == 1:
        pos[1] += 1
        came_from = [1, 0, 0, 0]
        return

    if came_from[3] == 0 and pipes[maze[pos[1]][pos[0]]][3] == 1:
        pos[0] -= 1
        came_from = [0, 1, 0, 0]
        return

with open("input.txt") as file:
    for index, line in enumerate(file.readlines()):
        line = line.strip()
        maze.append(line)

        if "S" in line:
            pos = [line.index("S"), index]

find_start()

while True:
    take_step()
    print(pos)

    steps += 1

    if maze[pos[1]][pos[0]] == "S":
        break

print(math.floor(steps/2))
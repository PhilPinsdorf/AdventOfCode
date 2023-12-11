import math
import numpy as np

maze = []
pos = [0, 0]
pipes = {"|": [1, 0, 1, 0], "L": [1, 1, 0, 0], "J": [1, 0, 0, 1], "F": [0, 1, 1, 0], "7": [0, 0, 1, 1], "-": [0, 1, 0, 1]}
came_from = [0, 0, 0, 0]
visited_positions = []
start_pipe = [0, 0, 0, 0]

def find_start():    
    global pos, came_from, start_pipe

    if pipes[maze[pos[1] + 1][pos[0]]][0] == 1:
        pos[1] += 1
        came_from = [1, 0, 0, 0]
        start_pipe = [0, 0, 1, 0]
        return

    if pipes[maze[pos[1]][pos[0] + 1]][1] == 1:
        pos[0] += 1
        came_from = [0, 1, 0, 0]
        start_pipe = [0, 0, 0, 1]
        return

    if pipes[maze[pos[1] - 1][pos[0]]][2] == 1:
        pos[1] -= 1
        came_from = [0, 0, 1, 0]
        start_pipe = [1, 0, 0, 0]
        return

    if pipes[maze[pos[1]][pos[0] - 1]][3] == 1:
        pos[0] -= 1
        came_from = [0, 0, 0, 1]
        start_pipe = [0, 1, 0, 0]
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
            visited_positions.append([pos[0], pos[1]])

find_start()
visited_positions.append([pos[0], pos[1]])

while True:
    take_step()

    visited_positions.append([pos[0], pos[1]])

    if maze[pos[1]][pos[0]] == "S":
        start_pipe = list(np.add(np.array(start_pipe), np.array(came_from)))
        break

start_char = [k for k, v in pipes.items() if v == start_pipe][0]
in_circle = False
last_corner = ""
tiles = 0

for line_index, line in enumerate(maze):
    for char_index, char in enumerate(line):
        if [char_index, line_index] in visited_positions:
            if char == "S":
                char = start_char
            
            match char:
                case "F":
                    last_corner = "F"
                case "L":
                    last_corner = "L"                  
                case "J":
                    if last_corner == "F":
                        in_circle = not in_circle  
                    last_corner = ""                
                case "7":
                    if last_corner == "L":
                        in_circle = not in_circle    
                    last_corner = ""               
                case "|":
                    in_circle = not in_circle
                    
            continue

        if in_circle:
            tiles += 1
    
print(tiles)
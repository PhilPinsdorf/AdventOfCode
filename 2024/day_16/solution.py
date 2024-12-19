from dataclasses import dataclass
from collections import defaultdict
import heapq

maze = []
start, end = (0, 0), (0, 0)
open_list, open_dict, closed_list = [], {}, set()
predecessors, costs = defaultdict(list), defaultdict(int)

@dataclass(order=True)
class Node:
    f: int
    g: int
    xy: tuple
    dir: int
    
DIRECTIONS = [
    ((1, 0), 1),  # Right
    ((-1, 0), 3),  # Left
    ((0, 1), 2),  # Down
    ((0, -1), 0)   # Up
]

f = open("test.txt", "r")
for index, line in enumerate(f):
    maze.append(list(line.strip()))
    
    if 'S' in line:
        start = (line.find('S'), index)
    if 'E' in line:
        end = (line.find('E'), index)

def heuristik(pos_xy, rotation):
    manhattan_distance = abs(end[0] - pos_xy[0]) + abs(end[1] - pos_xy[1])
    
    target_rotation = rotation
    if pos_xy[0] != end[0]:  # Horizontale Bewegung erforderlich
        target_rotation = 1 if end[0] > pos_xy[0] else 3
    elif pos_xy[1] != end[1]:  # Vertikale Bewegung erforderlich
        target_rotation = 2 if end[1] > pos_xy[1] else 0 
    
    min_rotations = min((target_rotation - rotation) % 4, (rotation - target_rotation) % 4)
    rotation_cost = min_rotations * 1000
    
    # Gesamtheuristik
    return manhattan_distance + rotation_cost

def expand_node(curr_node: Node):
    global open_list
    
    next_nodes = []
    for offset, direction in DIRECTIONS:
        next_x, next_y = curr_node.xy[0] + offset[0], curr_node.xy[1] + offset[1]
        if maze[next_y][next_x] != '#':
            next_nodes.append(((next_x, next_y), direction))
    
    for successor in next_nodes:
        successor_xy, successor_dir = successor[0], successor[1]
        
        if (successor_xy, successor_dir) in closed_list:
            continue
        
        tentative_g = curr_node.g + (min((curr_node.dir - successor_dir) % 4, (successor_dir - curr_node.dir) % 4) * 1000 + 1)
        
        if tentative_g < costs.get(successor_xy, float('inf')):
            costs[successor_xy] = tentative_g
            predecessors[successor_xy] = [curr_node.xy]  # Reset predecessors to only this path
        elif tentative_g == costs[successor_xy]:
            if curr_node.xy not in predecessors[successor_xy]:
                predecessors[successor_xy].append(curr_node.xy)
        
        successor_key = (successor_xy, successor_dir)
        if successor_key in open_dict:
            existing_successor = open_dict[successor_key]
            if tentative_g > existing_successor.g:
                continue
            del open_dict[successor_key]
        
        f = tentative_g + heuristik(curr_node.xy, curr_node.dir)
        node = Node(f, tentative_g, successor_xy, successor_dir)
        heapq.heappush(open_list, node)
        open_dict[successor_key] = node

def a_star():
    node = Node(0, 0, start, 1)
    heapq.heappush(open_list, node)
    while open_list:
        curr_node: Node = heapq.heappop(open_list)
        
        if curr_node.xy == end:
            print(curr_node.g)
            return True

        closed_list.add((curr_node.xy, curr_node.dir))
        expand_node(curr_node)
    return False
    
a_star()

def backtrack_iterative():
    stack = [end]
    positions = set()

    while stack:
        pos_xy = stack.pop()
        positions.add(pos_xy)

        for pre_pos in predecessors.get(pos_xy, []):
            if pre_pos not in positions:
                stack.append(pre_pos)

    return positions

positions = backtrack_iterative()
print(len(positions))

for index_y, line in enumerate(maze):
    new_line = ""
    for index_x, char in enumerate(line):
        if (index_x, index_y) in positions:
            new_line += "O"
        else:
            new_line += char
    print(new_line)
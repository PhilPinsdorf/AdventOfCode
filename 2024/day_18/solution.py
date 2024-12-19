from collections import defaultdict

blockers, size = [], 71
results = defaultdict(int)

f = open("input.txt", "r")
for line in f.readlines():
    splitted = list(map(int, line.strip().split(',')))
    blockers.append((splitted[0], splitted[1]))

def BFS(end):
    cut_blockers = blockers[:end]
    queue, explored, parents = [], set(), defaultdict(tuple)
    queue.append((0, 0))
    while queue:
        node = queue.pop(0)
        
        if node == (size - 1, size - 1):
            count = 0
            while node != (0, 0):
                node = parents[node]
                count += 1 
            return count
        
        edges = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  
        for dx, dy in directions:
            new_x, new_y = node[0] + dx, node[1] + dy
            if (0 <= new_x < size and 
                0 <= new_y < size and 
                (new_x, new_y) not in cut_blockers and 
                (new_x, new_y) not in explored):
                edges.append((new_x, new_y))
        
        for edge in edges:
            explored.add(edge)
            parents[edge] = node
            queue.append(edge) 
            
    return -1

bottom, top = 0, len(blockers)
while top - bottom > 1:
    mid = (bottom + top) // 2
    result = BFS(mid)
    
    if result == -1: top = mid
    else: bottom = mid

print(BFS(1024), blockers[top - 1])
count_1, count_2, id, pos = 0, 0, 0 ,0
disk_map_1, disk_map_2, free_space, block_length, block_start = [], [], [], {}, {}

line = open("input.txt", "r").readline()
for i, length in enumerate(list(map(int, line))):
    if i % 2 == 0:  # Block
        block_length[id] = length
        disk_map_1.extend([id] * length)
        block_start[id] = pos
        id += 1
    else:
        if length > 0:
            free_space.append((length, pos))
            disk_map_1.extend([-1] * length)
    pos += length

disk_map_2 = disk_map_1.copy()

i = 0
while i < len(disk_map_1):
    if disk_map_1[i] == -1:
        while disk_map_1[len(disk_map_1) - 1] == -1:
            disk_map_1.pop()
        element = disk_map_1.pop()
        disk_map_1[i] = element
    i += 1

curr_id = id - 1
while curr_id >= 0:
    first = block_start[curr_id]
    
    for index_free, (free_length, free_start) in enumerate(free_space):
        if free_start >= first: 
            break
        
        if free_length >= block_length[curr_id]:
            for i in range(block_length[curr_id]):
                disk_map_2[free_start + i] = curr_id
                disk_map_2[first + i] = -1 
            
            if free_length - block_length[curr_id] > 0:
                free_space[index_free] = (free_length - block_length[curr_id], free_start + block_length[curr_id])
            else:
                del free_space[index_free]
            break
    curr_id -= 1
    
for i in range(len(disk_map_1)):
    count_1 += i * disk_map_1[i]

for i in range(len(disk_map_2)):
    if disk_map_2[i] == -1:
        continue
    count_2 += i * disk_map_2[i]

print(count_1, count_2)
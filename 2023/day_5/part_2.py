seed_ranges = []
locations = []
map_overrides = [[], [], [], [], [], [], []]
curr_map = -1

with open("input.txt") as file:
    for index, line in enumerate(file.readlines()):
        line = line.strip()

        if index == 0:
            seeds = line[7:].split()
            for i in range(0, len(seeds), 2):
                seed_ranges.append([int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])])
            continue

        if line == "":
            curr_map += 1
            continue

        if not line[0].isdigit():
            continue

        source_destination = [int(a) for a in line.split()]
        map_overrides[curr_map].append(source_destination)

for i in range(7):
    next_ranges = []
    while len(seed_ranges) > 0:
        start, end = seed_ranges.pop()
        for dest_start, source_start, length in map_overrides[i]:
            overlap_start = max(int(start), int(source_start))
            overlap_end = min(int(end), int(source_start + length))
            if overlap_start < overlap_end:
                next_ranges.append([overlap_start - source_start + dest_start, overlap_end - source_start + dest_start])
                if overlap_start > start:
                    seed_ranges.append([start, overlap_start])
                if end > overlap_end:
                    seed_ranges.append([overlap_end, end])
                break
        else:
            next_ranges.append([start, end])

    seed_ranges = next_ranges
    

print(min(seed_ranges)[0])
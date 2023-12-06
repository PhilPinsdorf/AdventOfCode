seeds = []
locations = []
map_overrides = [[], [], [], [], [], [], []]
curr_map = -1

with open("input.txt") as file:
    for index, line in enumerate(file.readlines()):
        line = line.strip()

        if index == 0:
            seeds = line[7:].split()
            continue

        if line == "":
            curr_map += 1
            continue

        if not line[0].isdigit():
            continue

        source_destination = [int(a) for a in line.split()]
        map_overrides[curr_map].append(source_destination)

for seed in seeds:
    last_value = int(seed)
    for i in range(7):
        for rule in map_overrides[i]:
            if last_value >= rule[1] and last_value <= rule[1] + rule[2]:
                last_value = rule[0] + last_value - rule[1]
                break

    locations.append(last_value)

print(min(locations))
count_1, count_2 = 0, 0
sequences = []

f = open("test.txt", "r")
sequences = f.readline().strip().split(', ')
f.readline()
max_blocksize = max(list(map(len, sequences)))

def count_segmentations_recursive(line, memorization):
    if len(line) == 0:
        return 1

    if line in memorization:
        return memorization[line]

    total_count = 0

    for j in range(1, max_blocksize + 1):
        if j <= len(line):
            substring = line[:j]
            if substring in sequences:
                total_count += count_segmentations_recursive(line[j:], memorization)

    memorization[line] = total_count
    return total_count

for line in f:
    line = line.strip()
    count = count_segmentations_recursive(line, {})
    if count:
        count_1 += 1
    count_2 += count
    
print(count_1, count_2)
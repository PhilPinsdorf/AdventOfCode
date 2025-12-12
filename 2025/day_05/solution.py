from aoc_utils import read_input

data = read_input(use_test_file=False)

def solve_1():
    fresh_ids = set()

    seperator = data.index('')
    ranges = sorted([[int(y[0]), int(y[1])] for y in (x.split('-') for x in data[:seperator])], key=lambda x: x[0])
    ids = [int(x) for x in data[seperator + 1:]]

    for id in ids:
        for fresh_range in ranges:
            if fresh_range[0] <= id <= fresh_range[1]:
                fresh_ids.add(id)
                break

    return len(fresh_ids)

def solve_2():
    fresh_id_count = 0

    seperator = data.index('')
    ranges = sorted([[int(y[0]), int(y[1])] for y in (x.split('-') for x in data[:seperator])], key=lambda x: x[0])
    merged_ranges = []

    for i in range(len(ranges)):
        start = ranges[i][0]
        end = ranges[i][1]

        if merged_ranges and merged_ranges[-1][1] >= end:
            continue

        for j in range(i + 1, len(ranges)):
            if ranges[j][0] <= end:
                end = max(end, ranges[j][1])
        merged_ranges.append([start, end])

    for fresh_range in merged_ranges:
        fresh_id_count += fresh_range[1] - fresh_range[0] + 1

    return fresh_id_count

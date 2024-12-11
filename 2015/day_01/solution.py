count_1, count_2, found = 0, 0, False
line = open("input.txt", "r").readline()

for index, char in enumerate(list(line)):
    if char == '(':
        count_1 += 1
    if char == ')':
        count_1 -= 1
    if not found and count_1 == -1:
        count_2 = index + 1
        found = True

print(count_1, count_2)
count_1 = 0
count_2 = 0
f = open("input.txt", "r")
input = list(map(str.strip, f.readlines()))
possible = []

for index_l, line in enumerate(input):
    for index_c, char in enumerate(line):
        if char == 'X':
            possible.append(input[index_l][index_c:index_c+4]) # Right
            if index_c + 3 < len(line) and index_l + 3 < len(input):
                possible.append(''.join([input[index_l+i][index_c+i] for i in range(4)])) # Down Right
            if index_l + 3 < len(input):
                possible.append(''.join([input[index_l+i][index_c] for i in range(4)])) # Down
            if index_c - 3 >= 0 and index_l + 3 < len(input):
                possible.append(''.join([input[index_l+i][index_c-i] for i in range(4)])) # Down Left
            possible.append(input[index_l][index_c-3:index_c+1][::-1]) # Left
            if index_c - 3 >= 0 and index_l - 3 >= 0:
                possible.append(''.join([input[index_l-i][index_c-i] for i in range(4)])) # Up Left
            if index_l - 3 >= 0:
                possible.append(''.join([input[index_l-i][index_c] for i in range(4)])) # Up
            if index_c + 3 < len(line) and index_l - 3 >= 0:
                possible.append(''.join([input[index_l-i][index_c+i] for i in range(4)])) # Up Right
        
        if char == 'A':
            if index_c > 0 and index_l > 0 and index_c < len(line) - 1 and index_l < len(input) - 1:
                candidate = [[input[index_l - 1 + j][index_c - 1 + i] for i in range(3)] for j in range(3)]
                del candidate[0][1]
                del candidate[2][1]
                del candidate[1]

                if candidate in [[['M', 'M'], ['S', 'S']], [['S', 'M'], ['S', 'M']], [['S', 'S'], ['M', 'M']], [['M', 'S'], ['M', 'S']]]:
                    count_2 += 1
        
count_1 = possible.count('XMAS')
print(count_1, count_2)
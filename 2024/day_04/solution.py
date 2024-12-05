count_1, count_2 = 0, 0
f = open("test.txt", "r")
input = list(map(str.strip, f.readlines()))
candidates = []
directions = [ (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1) ]

for index_l, line in enumerate(input):
    for index_c, char in enumerate(line):
        if char == 'X':
            for dir_row, dir_col in directions:
                chars = []
                for i in range(4):
                    row, col = index_l + i * dir_row, index_c + i * dir_col
                    if 0 <= row < len(input) and 0 <= col < len(input[row]): 
                        chars.append(input[row][col])
                    else:
                        break
                if len(chars) == 4: candidates.append(''.join(chars))
        
        if char == 'A':
            if index_c > 0 and index_l > 0 and index_c < len(line) - 1 and index_l < len(input) - 1:
                candidate = [[input[index_l - 1 + j][index_c - 1 + i] for i in range(3)] for j in range(3)]
                del candidate[0][1]
                del candidate[2][1]
                del candidate[1]

                if candidate in [[['M', 'M'], ['S', 'S']], [['S', 'M'], ['S', 'M']], [['S', 'S'], ['M', 'M']], [['M', 'S'], ['M', 'S']]]:
                    count_2 += 1
        
count_1 = candidates.count('XMAS')
print(count_1, count_2)
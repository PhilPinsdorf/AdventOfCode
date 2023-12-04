f = open('input.txt', 'r')
lines = f.read().splitlines()
gamma = ''

for a in range(len(lines[0])):
    count = len([int(list(b)[a]) for b in lines if int(list(b)[a]) != 1])
    gamma += '0' if count > len(lines)/2 else '1'
epsilon = gamma.replace('0', 'x').replace('1', '0').replace('x', '1')

print(int(gamma, 2) * int(epsilon, 2))

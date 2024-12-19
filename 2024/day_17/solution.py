register = []
sequence = []
output = []
lines = open("input.txt", "r").readlines()
counter = 0

register.append(int(lines[0][12:]))
register.append(int(lines[1][12:]))
register.append(int(lines[2][12:]))
sequence = list(map(int, lines[4][9:].split(',')))

print(sequence)

def combo_calc(operand):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return register[0]      
        case 5:
            return register[1]
        case 6:
            return register[2]          

for i in range(100000000000000, 300000000000000, 100000000000000):
    register[0] = i
    register[1] = 0
    register[2] = 0
    counter = 0
    output = []
    
    while counter < len(sequence):
        opcode, operand = sequence[counter], sequence[counter + 1]
        combo = combo_calc(operand)
        
        match opcode:
            case 0:
                register[0] //= pow(2, combo)
            case 1:
                register[1] ^= operand
            case 2:
                register[1] = combo % 8
            case 3:
                if register[0] != 0:
                    counter = operand
                    continue
            case 4:
                register[1] ^= register[2]
            case 5:
                output.append(combo % 8)
            case 6:
                register[1] = register[0] // pow(2, combo)
            case 7:
                register[2] = register[0] // pow(2, combo)
                    
        counter += 2

    print(','.join(list(map(str, output))))

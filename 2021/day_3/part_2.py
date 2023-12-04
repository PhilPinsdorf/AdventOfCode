f = open('input.txt', 'r')
oxygen = f.read().splitlines()
co2 = oxygen

for a in range(len(oxygen[0])):
    if(len(oxygen) > 1):
        count = len([int(list(b)[a]) for b in oxygen if int(list(b)[a]) != 0])
        number = 1 if count >= len(oxygen)/2 else 0
        oxygen = list(filter(lambda b: int(list(b)[a]) != number, oxygen))

for a in range(len(co2[0])):
    if(len(co2) > 1):
        count = len([int(list(b)[a]) for b in co2 if int(list(b)[a]) != 0])
        number = 1 if count < len(co2)/2 else 0
        co2 = list(filter(lambda b: int(list(b)[a]) != number, co2))

print(int(oxygen[0], 2) * int(co2[0], 2))

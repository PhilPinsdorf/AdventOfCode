f = open("./input.txt", "r")
lines = f.read().splitlines()

result = map(lambda a, b: b > a, lines, lines[1:])
stripped = list(filter(lambda a: a != False, result))

print(len(stripped) + 1)

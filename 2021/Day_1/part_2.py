f = open("./input.txt", "r")
lines = f.read().splitlines()

window = list(map(lambda a, b, c: int(a) + int(b) + int(c), lines, lines[1:], lines[2:]))
result = list(map(lambda a, b: b > a, window, window[1:]))
stripped = list(filter(lambda a: a != False, result))

print(len(stripped))

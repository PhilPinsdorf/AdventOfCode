score = 0

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        numbers = ''.join(filter(str.isdigit, line.strip()))
        number = numbers[0] + numbers[-1]
        score += int(number)

print(score)
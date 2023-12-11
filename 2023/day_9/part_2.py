score = 0

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        numbers = [int(a) for a in line.split()]

        pyramid = [numbers]

        while True:
            next_step = []
            for i in range(len(pyramid[-1]) - 1):
                next_step.append(pyramid[-1][i + 1] - pyramid[-1][i])

            if next_step.count(0) == len(next_step):
                break
            else:
                pyramid.append(next_step)

        pyramid.reverse()

        next_number = 0
        for i in range(len(pyramid)):
            next_number = pyramid[i][0] - next_number 

        score += next_number
            
print(score)
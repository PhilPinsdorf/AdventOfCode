games = []

score = 0

with open("input.txt") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        games_strings = line.split(":")[1].split(";")

        drawings = []
        for game_string in games_strings:
            drawing = [0, 0, 0]
            drawing_strings = game_string.split(",")
            for drawing_string in drawing_strings:
                drawing_string = drawing_string.strip()
                number = int(drawing_string.split(" ")[0])

                if "red" in drawing_string:
                    drawing[0] = number

                if "green" in drawing_string:
                    drawing[1] = number

                if "blue" in drawing_string:
                    drawing[2] = number

                drawings.append(drawing)
        
        games.append(drawings)

for index, game in enumerate(games):
    minimum = [0, 0, 0]

    for drawing in game:
        for i in range(3):
            if drawing[i] > minimum[i]:
                minimum[i] = drawing[i]

    score += (minimum[0] * minimum[1] * minimum[2])

print(score)
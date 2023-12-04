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
    isValid = True

    for drawing in game:
        if drawing[0] > 12 or drawing[1] > 13 or drawing[2] > 14:
            isValid = False
    
    if isValid:
        score += (index + 1)

print(score)
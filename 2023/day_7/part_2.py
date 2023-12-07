from collections import defaultdict

categories = [[], [], [], [], [], [], []]
ranking = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
final = []
score = 0;

def condition(element):
    return ranking.index(element[0][0]), ranking.index(element[0][1]), ranking.index(element[0][2]), ranking.index(element[0][3]), ranking.index(element[0][4])

def find_categorie(occurencies):
    match len(occurencies):
            case 1:
                return 0
            case 2:
                return 1 if occurencies[0][1] == 4 else 2
            case 3:
                return 3 if occurencies[0][1] == 3 else 4
            case 4 | 5:
                return len(occurencies) + 1

with open("input.txt") as file:
    for line in file.readlines():
        hand = line.strip().split()

        tmp = hand[0].replace("J", "")

        if tmp == "":
            tmp = "K"

        lowest = []

        for distinct_char in list(set(tmp)):
            occurencies = defaultdict(int)

            for char in tmp:
                occurencies[char] += 1

            occurencies[distinct_char] += len(hand[0]) - len(tmp) 
            occurencies = sorted(occurencies.items(), key=lambda x:x[1], reverse=True)
            lowest.append(find_categorie(occurencies))

        categories[min(lowest)].append(hand)

for categorie in categories:
    final += sorted(categorie, key=condition, reverse=True)
final.reverse()

for index, hand in enumerate(final):
    score += int(hand[1]) * (index + 1)

print(score)
wins = []

with open("input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        winning_numbers = set(line[10:39].replace('  ', ' ').split()) 
        drawn_numbers = set(line[42:].replace('  ', ' ').split()) 

        wins.append(len(winning_numbers & drawn_numbers))

scratchcards = [1]*len(wins)

for index, scratchcard in enumerate(scratchcards):
    for i in range(index, index + wins[index]):
        scratchcards[i + 1] += scratchcard

print(sum(scratchcards))
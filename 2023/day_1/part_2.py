written_numbers = {"one": "on1e" , "two": "tw2o", "three": "thr3ee", "four": "fo4ur", "five": "fi5ve", "six": "si6x", "seven": "sev7en", "eight": "eig8ht" , "nine": "ni9ne"}
score = 0

with open("input.txt") as file:
    lines = file.readlines()

    for line in lines:
        line = line.strip()
        for written_number in written_numbers:
            line = line.replace(written_number, written_numbers[written_number])

        print(line)
        numbers = ''.join(filter(str.isdigit, line.strip()))
        print(numbers)
        number = numbers[0] + numbers[-1]
        print(number)
        print(" ")
        score += int(number)

print(score)
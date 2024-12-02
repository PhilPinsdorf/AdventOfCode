count_1 = 0
count_2 = 0

def check_level(numbers) -> bool:
    numbers_srt = sorted(numbers)
    numbers_rev = sorted(numbers, reverse=True)
    
    if numbers not in (numbers_srt, numbers_rev):
        return False
    
    for i in range(1, len(numbers)):
        distance = abs(numbers[i - 1] - numbers[i])
        if distance > 3 or distance == 0:
            return False
    
    return True

f = open("input.txt", "r")
for line in f:
    numbers = list(map(int, line.split()))
    candidates = [numbers[:i] + numbers[i+1:] for i in range(len(numbers))]
    
    if check_level(numbers):
        count_1 += 1
    
    for candidate in candidates:
        if check_level(candidate):
            count_2 += 1
            break

print(count_1, count_2)
first_numbers = []
second_numbers = []
count_1 = 0
count_2 = 0

f = open("test.txt", "r")
for line in f:
  line = line.split()
  first_numbers.append(int(line[0]))
  second_numbers.append(int(line[1]))

first_numbers.sort()
second_numbers.sort()

for num in range(len(first_numbers)):
  count_1 += abs(first_numbers[num] - second_numbers[num])

for num in first_numbers:
  count_2 += num * second_numbers.count(num)

print(count_1)
print(count_2)
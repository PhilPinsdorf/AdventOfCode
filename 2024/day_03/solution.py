import re 

count1 = 0
count2 = 0
enabled = True

f = open("input.txt", "r")
for line in f:
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", line)

    for match in matches:
        if match[2]:
            enabled = True
            continue
        if match[3]:
            enabled = False
            continue
        
        count1 = count1 + int(match[0]) * int(match[1])
        
        if enabled:
            count2 = count2 + int(match[0]) * int(match[1])

print(count1, count2)

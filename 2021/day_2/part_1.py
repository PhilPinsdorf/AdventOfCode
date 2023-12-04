import re

f = open('input.txt', 'r')
txt = f.read()

pattern = re.compile(r"forward ([1-9]+)|up ([1-9]+)|down ([1-9])")
match = re.findall(pattern, txt)

fw = sum([int(item[0]) for item in match if item[0] != ''])
up = sum([int(item[1]) for item in match if item[1] != ''])
dw = sum([int(item[2]) for item in match if item[2] != ''])

print(fw * (dw - up))

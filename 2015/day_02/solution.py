count_1, count_2 = 0, 0

f = open("input.txt", "r")

for line in f:
    lwh = list(map(int, line.split('x')));
    l, w, h = lwh[0], lwh[1], lwh[2];
    lw, wh, lh = l*w, w*h, l*h;
    sides_square = [lw, wh, lh]
    smallest = min(sides_square)
    count_1 += 2*lw + 2*wh + 2*lh + smallest;
    
    bow = l * w * h
    sides = [l, w, h]
    sides.remove(max(sides))
    count_2 += 2 * sides[0] + 2 * sides[1] + bow

print(count_1, count_2)
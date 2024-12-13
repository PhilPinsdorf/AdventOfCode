import re
score_1, score_2 = 0, 0 

f = open("input.txt", "r")
lines = list(filter(None, list(map(str.strip, f.readlines()))))

def calc_cramer(i, longer):
    Ax, Ay = tuple(map(int, re.findall(r'X\+(\d+), Y\+(\d+)', lines[i * 3 + 0])[0]))
    Bx, By = tuple(map(int, re.findall(r'X\+(\d+), Y\+(\d+)', lines[i * 3 + 1])[0]))
    Cx, Cy = tuple(map(int, re.findall(r'X\=(\d+), Y\=(\d+)', lines[i * 3 + 2])[0]))
    if longer: Cx, Cy  = 10000000000000 + Cx, 10000000000000 + Cy

    A = (Cx * By - Bx * Cy) / (Ax * By - Bx * Ay) 
    B = (Ax * Cy - Cx * Ay) / (Ax * By - Bx * Ay) 

    if A % 1 == 0.0 and B % 1 == 0.0:
        return int(A), int(B)
    return 0, 0

for i in range(len(lines) // 3):
    A, B = calc_cramer(i, False)
    score_1 += A * 3 + B

    A, B = calc_cramer(i, True)
    score_2 += A * 3 + B

print(score_1, score_2)
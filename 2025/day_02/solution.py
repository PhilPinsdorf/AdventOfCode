from aoc_utils import read_input

data = read_input(use_test_file=False, separator=",")
print(data)

def solve_1():
    solution = 0
    
    for num_range in data:
        start, stop = num_range.split("-", 1)
        
        for num in range(int(start), int(stop) + 1):
            s_num = str(num)
            l_total = len(s_num)

            if l_total % 2 != 0:
                continue

            first, second = s_num[:int(l_total/2)], s_num[int(l_total/2):]
            
            if first == second:
                solution += num

    return solution

# Besserer Ansatz: Mögliche Zahlen generieren, die in dem Raum liegen statt sie zu suchen.
def solve_2():
    solution = 0

    for num_range in data:
            start, stop = num_range.split("-", 1)

            for num in range(int(start), int(stop) + 1):
                s_num = str(num)
                l_total = len(s_num)  

                for chunk_size in range(1, l_total):
                    if l_total % chunk_size == 0:
                        
                        split_list = [s_num[i : i + chunk_size] for i in range(0, l_total, chunk_size)]

                        if all(x == split_list[0] for x in split_list):
                            solution += num
                            break

    return solution
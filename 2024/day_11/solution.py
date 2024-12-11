from collections import Counter
count_1, count_2 = 0, 0
nums = list(map(int, open("input.txt", "r").readline().split()))
occuring = Counter(nums) # Behaves like defaultdict + Already has a counting occurences in list initialization Constuctor built in  

for i in range(75):
    dict_copy = occuring.copy()
    for key, value in dict_copy.items():
        occuring[key] -= value
        
        if key == 0:
            occuring[1] += value
            continue
        
        str_key = str(key)
        str_len = len(str_key)
        if str_len % 2 == 0:
            half = str_len // 2 # Floor division
            occuring[int(str_key[half:])] += value
            occuring[int(str_key[:half])] += value
        else:
            occuring[key * 2024] += value

    if i == 24: count_1 = sum(occuring.values())
    if i == 74: count_2 = sum(occuring.values())

print(count_1, count_2)
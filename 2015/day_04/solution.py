import hashlib

line = open("input.txt", "r").readline()

for i in range(100000000):
    result = hashlib.md5((line + str(i)).encode())
    
    if result.hexdigest()[:5] == "00000":
        print(result.hexdigest(), i)
        break

for i in range(100000000):
    result = hashlib.md5((line + str(i)).encode())
    
    if result.hexdigest()[:6] == "000000":
        print(result.hexdigest(), i)
        break

def euclid(a,b):
    x = int(a)
    y = int(b)
    while y != 0:
        x, y = y, x % y
    return x
        
def coprime(a,b):
    result = euclid(a,b)
    if result == 1:
        return True
    else:
        return False

import random

count_true = 0

for _ in range(100000):
    a = random.randint(1, 10000)
    b = random.randint(1, 10000)
    if coprime(a,b):
        count_true += 1
    
print(count_true)

result_final = count_true / 100000

print(result_final)
def prime_number(n):
    if n <= 1:
        return False
    for j in range(2, 1 + int(n**(1/2))):
        if n % j == 0: 
            return False
    return True

a = int(input("nの値を入力: "))

if prime_number(a):
    print("nは素数です")
else:
    print("nは素数ではない")
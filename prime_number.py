a = input("nの値を入力: ")

def prime_number(n):
    for j in range(2, n+1):
        if n % j != 0:
            continue
    if j != int(a):
        return False
    if j == int(a):
        return True
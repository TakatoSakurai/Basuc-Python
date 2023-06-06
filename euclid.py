a = input("a の値を入力: ")
b = input("b の値を入力: ")

def euclid(a,b):
    x = int(a)
    y = int(b)
    while y != 0:
        x, y = y, x % y
    return x
        
def coprime(a,b):
    x = int(a)
    y = int(b)
    while y != 0:
        x, y = y, x % y
    if x == 1:
        return True
    else:
        return False

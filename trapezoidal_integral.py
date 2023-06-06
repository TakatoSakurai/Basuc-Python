import math
# --example--
# print(sin(0))
# >>> 0
# -----------

a = float(input("aの値を入力：") or 0)
b = float(input("bの値を入力：") or 1)
n = int(input("nの値を入力：") or 100)
f = input("関数を入力:")
h = (b - a) / n
def function(x):
    return eval(f)

def integral(f,a,b,n):
    S = 0
    for i in range(1, n+1):
        S += (function(a + (i - 1) * h) + function(a + i * h)) / 2
    S *= h
    return S
result = integral(f,a,b,n)
print(result)
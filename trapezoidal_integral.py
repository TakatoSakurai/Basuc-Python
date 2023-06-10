import math
# --example--
# print(sin(0))
# >>> 0
# -----------

def integral(f,a,b,n):
    S = 0
    h = (b - a) / n
    for i in range(1, n+1):
        S += (f(a + (i - 1) * h) + f(a + i * h)) / 2
    S *= h
    return S

#1
print(integral(math.sin, 0, math.pi/2, 50))

# 2
def function1(x):
    return 4 / (1 + math.pow(x, 2))

print(integral(function1, 0, 1, 100))

# 3
def function2(x):
    return math.pi**(1/2) * math.exp(-math.pow(x, 2))

print(integral(function2, -100, 100, 1000))
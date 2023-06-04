import math
from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = math.pi / 2
n = 100
h = (b - a) / n
S = 0
for i in range(1, n + 1):
    S += (sin(a + (i - 1) * h) + sin(a + i * h)) / 2
S *= h

print(S)
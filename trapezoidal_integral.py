from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
s2 = 0
for i in range(0, 100):
    y1 = (1 - (i/100) ** 2) ** (1/2)
    y2 = (1 - ((i + 1)/100) ** 2) ** (1/2)
    s1 = (1/100) * (y1 + y2) * (1/2)
    s2 += s1
print(str(s2))
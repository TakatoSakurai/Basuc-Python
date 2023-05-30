a = input("aの値を入力: ")
b = input("bの値を入力: ")
a = int(a)
i = a + 1
for j in range(2, i):
    if a % j != 0:
        continue
    if j == a:
         print(str(a) + 'は素数です')
    if j != a:
        print(str(a) + 'は素数でない')
        break
a = input("a の値を入力: ")
b = input("b の値を入力: ")

x = int(a)
y = int(b)
if x > y:
    x1 = x
    y1 = y
    y2 = x1 % y1
    while y2 != 0:
        x1 = y1
        y1 = y1 % y2
    print('最大公約数は' + str(x1 // y1))
elif y > x:
    x1 = y
    y1 = x
    y2 = x1 % y1
    while y2 != 0:
        x1 = y1
        y1 = y1 % y2
    print('最大公約数は' + str(x1 // y1))
else:
    print('最大公約数は' + str(x))
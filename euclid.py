a = input("a の値を入力: ")
b = input("b の値を入力: ")

x = int(a)
y = int(b)
while y != 0:
    x, y = y, x % y

print('最大公約数は' + str(x))
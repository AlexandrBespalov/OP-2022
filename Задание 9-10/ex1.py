from random import randint

m = int(input("Введите кол-во строк "))
n = int(input("Введите кол-во стоблцов "))

print("Элементы массива:")
a = [[randint(1,21) for j in range(n)] for i in range(m)]
for i in range(m):
    print(a[i], max(a[i]))
for i in range(n):
    x=[x[i] for x in a]
    print(min(x), end = " ")
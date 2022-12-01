a = int(input())

b = a - 1
while a < 2:
    print('Число должно быть больше 2-х!')
    a = int(input())

while a % b != 0:
    b = b - 1

if a % b == 0:
    b = a // b
    print(b)
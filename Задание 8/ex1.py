from math import gcd

nod = lambda x, y: gcd(x, y)
nok = lambda x, y: x * y / nod(x, y)

while True:
    x, y = map(int, input('m n >>').split()); NOD = nod(x, y)
    print('НОД(m, n) =', NOD); print('НОК(m, n) =', x * y // NOD)
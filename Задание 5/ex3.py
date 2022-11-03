from math import log

x = int(log(int(input()), 2))
i = 1

for i in range(x):
    i *= 2

print(x, i)
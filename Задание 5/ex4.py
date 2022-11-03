x = int(input())
y = int(input())

n = 1

while x <= y:
    if x == y:
        break
    x += x / 10
    n += 1

print(n)
i = int(input())
x = 0

while i != 0:
    next = int(input())
    if next != 0 and i < next:
        x += 1
    i = next

print(x)
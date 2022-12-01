a = int(input())
c = 1
b = 1

while True:
    x = int(input())
    if x == a:
        if x == 0:
            break
        c += 1
    else:
        if c > b:
            b = c
        a = x
        c = 1
    
print(b)
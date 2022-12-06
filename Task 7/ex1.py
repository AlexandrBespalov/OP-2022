mas=[]
 
for value in range(10):
    value = int(input("Введите элемент массива: "))
    mas.append(value)
 
element = max(mas)
print('Наибольший элемент массива: ',element)
 
b = 0
m = 0
r = 0

for i in mas:
    if i > element:
        print(i,">",element)
        b += 1
    elif i < element:
        print(i,"<",element)
        m += 1
    elif i == element:
        print(i,"<",element)
        r += 1

print("Элементов > ",b)
print("Элементов < ",m)
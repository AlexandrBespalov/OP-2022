from random import randint

def func():

    with open('ex1_input.txt', 'r') as f:
       a = [[int(num) for num in line.split(',')] for line in f]
    print(a)

    m = int(input("Введите кол-во строк "))
    n = int(input("Введите кол-во стоблцов "))

    print("Элементы массива:")
    a = [[randint(1,21) for j in range(n)] for i in range(m)]
    for i in range(m):
        print(a[i], max(a[i]))
    for i in range(n):
        x = [x[i] for x in a]
        print(min(x), end = " ")

    with open("ex1_output.txt", "w") as file:
        print( file=file, sep=",\n", end="\n") #есть вопросы с выводом в отдельный файл 11-16 строки

func()
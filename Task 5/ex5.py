array = [3,5,5,4,2,7,6,0,6,3]

def func():
    result = 0
    for i in range(len(array)):
        if array[i] < 0:
            continue

        if array[i] != 0:
            result+=1
        else:
            print(f"Кол-во членов в последовательности {result}")

func()
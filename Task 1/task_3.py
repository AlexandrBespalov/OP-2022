def func():
    age = int(input("Введите возраст"))

    if age > 0 and age < 75:
        print("Подходящий возраст")
    else:
        print("Вы нам не подходите")
        return

    if age >= 16:
        print("Поздравляем вы поступили в ВГУИТ!")
    else:    
        print("Закончите школу школу!")
        a = 16 - age
        print("Приходите через: ", a)

        return

    name = input("Введите имя")

    if name == "Иван":
        print("Поздравляем с тем, что Вы - Иван!") 
        return

func()
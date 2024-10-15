

# Homeworck 5.2
continuaInput = "Y"
while continuaInput == "Y" : # калькулятор повторяеся пока continuaInput == "Y"
    a = int(input("Enter First number: ")) #Ввод числел для вычислений
    b = int(input("Enter Second number: "))

    user_select = input("Chouse from - + / *. and press enter: ") # выбор действия

    match user_select: #
            case ("-"): #
                print( a - b)# вычисление и вывод в консоль результата
            case ("+"):
                print(a + b)
            case ("*"):
                print(a * b)
            case ("/"):
                if b == 0:
                    b = int(input("Invalid number, select enother number: ")) # перевірка ділення на 0, з мозжливістю виправитись
                print( a / b)
            case _:
                print("Invalid input please try again")

    continuaInput = input("do you want to continua Y/N?: ") # запрос на продолжение работы с калк. и перезапись переменной continuaInput
    continuaInput.upper()


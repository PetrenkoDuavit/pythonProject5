# # Homeworck 5.2
# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.

import string
import keyword

test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', '3m', 'm3', 'assert', 'assert_exception', 'some_super_puper__value']

for test_variable in test_data:
    print(len(test_variable))
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:
            print(f"Error! Found {test_variable} 1111is keyword!") # добавил 111 чтобы понимать какая срабатывает, я потом уберу
        elif not test_variable[0].isnumeric() and test_variable.count(" ") == 0:# если сюда добавить  and test_variable.islower(), "_" не проходит эту проверку
            is_correct = True
            for symbol in string.punctuation.replace("_", ""):
                if symbol in test_variable:
                    is_correct = False
                    print(f"Error! Found {test_variable} 2222in variable name!")
                    break
        start_index = 0 # цикл работает только если подряд идут нижние подчеркиввния, остальных случаях он будет безконечным,
        while start_index < len(test_variable) - 1 :
            first_underscore_index = test_variable.find("_")
            if first_underscore_index != -1 and len(test_variable) >= 2:
                second_underscore_index = test_variable.find("_", first_underscore_index + 1)
                if second_underscore_index != -1 and second_underscore_index - first_underscore_index == 1:
                    is_correct = False
                    print(f"Error! Found double '_' in {test_variable} 33333variable name!")
                    break
                else:
                    start_index = first_underscore_index + 1
            else:
                start_index = first_underscore_index + 1

        if is_correct:  # эта переменная почемуто не связана с остальными is_correct
                print(f"Keyword {test_variable} is correct!")
        else:
            print(f"Error! Found {test_variable} in 4444variable name!")
    else:
        print("Incorrect variable length!")


# import string

# # Homeworck 5.2
# continuaInput = "Y"
# while continuaInput == "Y" : # калькулятор повторяеся пока continuaInput == "Y"
#     a = int(input("Enter First number: ")) #Ввод числел для вычислений
#     b = int(input("Enter Second number: "))
#
#     user_select = input("Chouse from - + / *. and press enter: ") # выбор действия
#
#     match user_select: #
#             case ("-"): #
#                 print( a - b)# вычисление и вывод в консоль результата
#             case ("+"):
#                 print(a + b)
#             case ("*"):
#                 print(a * b)
#             case ("/"):
#                 if b == 0:
#                     b = int(input("Invalid number, select enother number: ")) # перевірка ділення на 0, з мозжливістю виправитись
#                 print( a / b)
#             case _:
#                 print("Invalid input please try again")
#
#     continuaInput = input("do you want to continua Y/N?: ") # запрос на продолжение работы с калк. и перезапись переменной continuaInput
#     continuaInput.upper()

 # Homeworck 5.3
# # "Python Community", "i like python community!", "t!e@s#t t%e^s&t"
# inputForHashTag =  input("Enter string: ")
# titelHashtag = ""
# hashTag =""
#
# if inputForHashTag == "": # проверка присутствия символов
#     print("False")
# elif len(inputForHashTag) > 140: # символов не должно быть больше 140
#         print("To many symbols, must bee less than 140")
# else:
#     titelHashtag = inputForHashTag.title() # слова должны начинатся с заглавной буквы
#     for char in titelHashtag:# добавляю только те символы который не содержат знаки из string.punctuation
#         if char not in string.punctuation:
#             hashTag = hashTag + char
# print( "#" + hashTag.replace(" ", "")) # добавляю "#" в начало, и удаляю пробелы

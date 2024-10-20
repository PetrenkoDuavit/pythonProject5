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
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:  # проверка ключевых слов
            print(f"Error! Found {test_variable} is keyword!")
        elif  not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0: # проверка, первый символ не должен содержать цифр, без заглавных букв и без пробелов
            is_correct = True
            for symbol in string.punctuation.replace("_", ""):  # удаляем все "_" что бы исключить "_" из проверки
                if symbol in test_variable:
                    is_correct = False
                    print(f"Error! Found {test_variable} in variable name!")
                    break

            first_underscore_index = test_variable.find("__")  # поиск дублей "__"
            if first_underscore_index != -1:
                    is_correct = False
                    print(f"Error! Found double '_' in {test_variable} variable name!")

            if is_correct:
                print(f"Keyword {test_variable} is correct!")
        else:
            print(f"Error! Found {test_variable} in 111variable name!")
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

"""
Пользователь вводит число, 
затем вводит второе число.
Затем программа выводит на экран сумму этих чисел, НО
В таком формате:

10 + 5 = 15
"""
number1 = input('Введите 1 число: ')
number2 = input('Введите 2 число: ')

result = int(number1) + int(number2)

print(number1 + ' + ' + number2 + ' = ' + str(result))

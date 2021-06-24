# Пользователь вводит 5 чисел. Найти, сколько из них чётные.

numbers_amount = int(input('Сколько чисел вы хотите ввести: '))
count = 0

a = 0
while a < numbers_amount:
    number = int(input('Введите число №' + str(a + 1) + ': '))

    if number % 2 == 0:
        count += 1
    
    a += 1

print(count)

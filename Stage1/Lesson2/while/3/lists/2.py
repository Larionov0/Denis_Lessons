# Вывести все числа списка, которые меньше 5

numbers = [5, 3, 6, 6, 2, 6, 1, 7, 4, 13]

i = 0
while i < len(numbers):
    if numbers[i] < 5:
        print(numbers[i])
    i += 1


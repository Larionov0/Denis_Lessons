# Пользователь вводит имена. Вывести, в скольких именах
# есть буква "а"


count = 0
while True:
    name = input('Введите имя: ')

    if name == 'стоп':
        break
    else:
        if 'а' in name or 'А' in name:
            count += 1

print(count)

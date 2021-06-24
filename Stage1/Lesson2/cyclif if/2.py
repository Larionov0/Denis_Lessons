# Пользователь вводит 5 слов
# Вывести количество маленьких, средних и больших слов
# Маленькое, если длина слова <= 4
# Среднее, если 4 < длина <= 8
# Большое, если длина > 8

w1 = input('Слово №1: ')
w2 = input('Слово №2: ')
w3 = input('Слово №3: ')
w4 = input('Слово №4: ')
w5 = input('Слово №5: ')

s_count = 0
m_count = 0
l_count = 0

if len(w1) <= 4:
    s_count += 1
elif len(w1) <= 8:
    m_count += 1
else:
    l_count += 1


if len(w2) <= 4:
    s_count += 1
elif len(w2) <= 8:
    m_count += 1
else:
    l_count += 1


if len(w3) <= 4:
    s_count += 1
elif len(w3) <= 8:
    m_count += 1
else:
    l_count += 1


if len(w4) <= 4:
    s_count += 1
elif len(w4) <= 8:
    m_count += 1
else:
    l_count += 1


if len(w5) <= 4:
    s_count += 1
elif len(w5) <= 8:
    m_count += 1
else:
    l_count += 1


print('Маленьких:', s_count)
print('Средних', m_count, sep=':')  # sep - отвечает за разделитель при склеивании в функции print
print('Больших', l_count, sep=':')

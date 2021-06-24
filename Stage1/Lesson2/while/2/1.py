# НЕВЕРНЫЙ КОД! Не соблюдается принцип DRY (происходит повторение своего кода)

print(' ' * 10 + '_' * 15)
password = input('Пароль   |')
while password != 'lol123':
    print('Пароль неверный!')
    print(' ' * 10 + '_' * 15)
    password = input('Пароль   |')

print('Secret')

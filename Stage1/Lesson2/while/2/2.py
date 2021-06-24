while True:
    print(' ' * 10 + '_' * 15)
    login = input('Логин    |')
    print(' ' * 10 + '_' * 15)
    password = input('Пароль   |')

    if password == 'lol123' and login == 'user':
        break
    else:
        print('Такого пользователя нету! Попробуйте еще раз')

print('Secret')

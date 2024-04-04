while 1:
    print()
    name=input('Ваше имя: ')
    if bool(name):
        print(f'Привет, {name}!')
    else:
        print('Вы не ввели имя.')
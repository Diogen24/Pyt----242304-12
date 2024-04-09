while 1:
    number=input('Введите число: ')
    try:
        number=float(number)
    except:
        print('Ошибка ввода')
        continue
    if number%1==0:
        number=int(number)
    if number%3==0:
        print(f'Число {number} делится на 3')
    elif number>10:
        print(f'Число {number} больше 10')
    else:
        print(f'Число {number} не соответствует условиям')
    print('')
while 1:
    number=input('Введите целое число: ')
    try:
        number=int(number)
    except:
        print('Не целое число')
        continue
    print('Все числа от 0 до введенного числа включительно: ')
    for i in range(number+1):
        print(i)
    print('')
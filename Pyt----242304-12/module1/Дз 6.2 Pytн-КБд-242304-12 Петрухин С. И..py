while 1:
    number=input('Введите целое число: ')
    try:
        number=int(number)
    except:
        print('Не целое число')
        continue
    print('Все числа от 0 до введенного числа включительно: ')
    i=0
    while i<=number:
        print(i)
        i+=1
    print('')
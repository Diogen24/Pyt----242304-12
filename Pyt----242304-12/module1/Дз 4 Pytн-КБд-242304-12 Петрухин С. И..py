print('Здравствуйте! Это программа для определения совершеннолетия.')
while 1:
    print()
    age=input('Ваш возраст: ')
    try:
        int(age)
    except:
        print('Ошибка ввода')
        continue
    age=int(age)
    if age<0:
        print('Ошибка ввода')
        continue
    if age<18:
        print('Вы несовершеннолетний(я)')
    else:
        print('Вы совершеннолетний(я)')
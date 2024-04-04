while 1:
    print()
    print('Эта программа предназначена для определения стоимости билета в кинотеатр')
    age=input('Введите возраст: ')
    try:
        int(age)
    except:
        print("Неверно введён возраст!")
        continue
    age=int(age)
    if age<12:
        print('Билет бесплатный')
        continue
    elif 12<=age<18:
        escort=input('Наличие сопровождающего?(введите "да" при наличии) ')
        if escort=='да' or escort=='Да' or escort=='ДА' or escort=='дА':
            print('Билет со скидкой')
            continue
        else:
            print('Полная стоимость билета')
            continue
    else:
            print('Полная стоимость билета')
            continue
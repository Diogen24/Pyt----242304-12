print('Здравствуйте! Эта программа представляет собой простой калькулятор')
#Простой цикл для повторения выполнения программы
while 1:
    print('')
    print('Доступные для выполнения операции: "+", "-", "*", "/"')
    operation=input('Введите какую операцию надо совершить: ')
    #Проверка допустимости операции, если нет, то совершается переход в начало цикла "while"
    if operation!='+' and operation!='-' and operation!='*' and operation!='/':
        print('Недопустимая операция!')
        continue
    a=input('Введите первое число: ')
    #Является ли a числом, если нет, то совершается переход в начало цикла "while"
    try:
        float(a)
    except:
        print("Это не число")
        continue
    a=float(a)
    b=input('Введите второе число: ')
    #Является ли b числом, если нет, то совершается переход в начало цикла "while"
    try:
        float(b)
    except:
        print("Это не число")
        continue
    b=float(b)
    if operation=='+':
        result=float(a+b)
    elif operation=='-':
        result=float(a-b)
    elif operation=='*':
        result=float(a*b)
    elif operation=='/':
        #Проверка того, не равен ли знаменатель нулю и если равен
        #совершается переход в начало цикла "while"
        if b==0:
            print('На ноль делить нельзя!')
            continue
        result=float(a/b)
    print(f'Результат равен {result}')
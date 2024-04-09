print('Список из 10 элементов с разными типами данных (строки, числа и булевы значения): ')
spisok=[False, 1, 2.1, True, 3, 4, 5, 6, 7, 8]
print(spisok)
print('Первые 5 элементов списка: ')
first_5=spisok[0:5]
print(first_5)
print('Последние 3 элемента списка: ')
last_3=spisok[-3:]
print(last_3)
print('Каждый второй элемент списка: ')
every_2=spisok[1::2]
print(every_2)
print('Новое значение для третьего элемента списка и весь измененный список: ')
spisok[2]=100
print(spisok)
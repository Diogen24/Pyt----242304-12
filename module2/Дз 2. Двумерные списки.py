# Двумерные списки
# Цель: Закрепить полученные знания и решить практические задачи с использованием двумерных списков.
# Что нужно сделать: 
# Домашнее задание 2
# Напишите программу, которая создает двумерный массив размером 3x3 и заполняет его числами от 1 до 9. 
# Затем программа должна выводить строку из элементов каждой строки массива.
matrix=[]
t=0
for row in range(3):
    matrix.append([i+1 for i in range(t,t+3)])
    t+=3
#print(matrix)
for row in range(3):
    for column in range(3):
        print(matrix[row][column], end=' ')

#Приветствие
print('Здравствуйте!')
#Объявление и ввод переменных с данными об имени
first_name=input('Введите ваше имя: ')
last_name=input('Введите вашу фамилию: ')
#Импорт класса date из модуля datetime для вычисления возраста
from datetime import date
#Получение сегодняшней даты
today=date.today()
#Объявление и ввод переменных содержащий информацию о дате рождения
birthday=int(input('Введите число вашей даты рождения: '))
birthmonth=int(input('Введите месяц вашей даты рождения: '))
birthyear=int(input('Введите год вашей даты рождения: '))
#Вычисление возраста с учетом того, прошел ли в этом году день рождения
age=today.year-birthyear-((today.month, today.day)<(birthmonth, birthday))
#Вывод с использованием f-строки фамилии, имени, и вычисленного возраста
print(f'Вас зовут {last_name} {first_name} и вам {age} лет')
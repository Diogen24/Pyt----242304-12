# Введение в ООП. Классы и объекты.
# Цель: Закрепить на практике работу с классами и объектами, 
# научиться самостоятельно писать код в соответствии с парадигмой ООП.
# Что нужно сделать: 
# Домашнее задание 3
# Создайте класс `Car`, который имеет атрибуты `make` (марка автомобиля), 
# `model` (модель автомобиля) и `year` (год выпуска). 
# Дайте им также метод `display_info()`, который выводит информацию о машине (марка, модель и год).
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def display_info(self):
        print(f'Марка: {self.make}, модель: {self.model}, год выпуска: {self.year}')
        
car1=Car('ВАЗ','2101',1989)
car1.display_info()
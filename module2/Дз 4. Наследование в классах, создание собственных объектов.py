# Наследование в классах, создание собственных объектов.
# Цель: Изучить создание собственных объектов и наследование в классах на практике, выполнив задания.
# Что нужно сделать: 
# Домашнее задание 4
# Создайте родительский класс `Animal` с атрибутами `name` и `species`. 
# Дайте им также метод `make_sound()`, который выводит звук, издаваемый животными.
# Создайте подклассы `Dog` и `Cat`, которые наследуют от класса `Animal`. 
# Дайте каждому из них свой собственный метод `make_sound()`, 
# который выводит соответствующий звук (`"Гав"` для собаки и `"Мяу"` для кота).
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(f'{self.name} говорит "Гав"')
        
class Cat(Animal):
    def make_sound(self):
        print(f'{self.name} говорит "Мяу"')
        
dog1=Dog('Шарик','Собака')
cat1=Cat('Матроскин','Кот')

dog1.make_sound()
cat1.make_sound()
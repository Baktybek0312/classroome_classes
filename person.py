# Класс Person
# a) поля fullName, age, place(address)
# б) методы move() и talk(), в которых просто вывести на консоль сообщение -"Такой-то  Person говорит".
# метод move будет менять его положение
# в) Добавьте  конструктор  с двумя параметрами fullName, address, age = 18
# г)метод __str__ настроить как он будет отображаться

class Person:
    def __init__(self, full_name, address, age=18):
        self.full_name = full_name
        self.age = age
        self.address = address

    def move(self, address) :
        self.address = address

    def talk(self) :
        print(f'{self.full_name} говорит')

    def __str__(self) :
        return f'{self.full_name} в городе {self.address} возраст {self.age}'


per = Person("Токтобеков Бактыбек Муратбекович", "г.Бишкек", 25)
per.talk()
per.move("Нарын")
print(str(per))

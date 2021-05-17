# Класс Phone
# а) Создайте класс Phone, который содержит атрибуты number, model и weight.
# б) Создайте три экземпляра этого класса.
# в) Выведите на консоль значения их атрибутов.
# г) Добавить конструктор в класс Phone, который принимает на вход три параметра для инициализации переменных класса - number, model и weight.
# д) Создать метод sendMessage. Данный метод принимает на вход номера телефонов, которым будет отправлено сообщение.
# Метод выводит на консоль номера этих телефонов.
from pyexpat import model


class Phones:
    def __init__(self,  number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def sendMessage(self, number, model, weight):
        print("Вам отправили с номера:", number,model,weight)

iphone = Phones(996755557055 ,"Iphone 11",255)
samsung = Phones(996550905992,"Samsung S10", 155)
xiaomi = Phones(99670455557055,"Xiaomi mi8Lite", 125)
iphone.sendMessage(samsung.number,samsung.model,samsung.weight)
samsung.sendMessage(xiaomi.number,xiaomi.model,xiaomi.weight)
xiaomi.sendMessage(iphone.number,iphone.model,iphone.weight)


# class Car:
#     #Статические поля
#     door = 4
#     wheelse = 4
#     role = 1
#     window = 6
#     #Динамические поля
#     def __init__(self, year, mark):
#         self.year = year
#         self.mark = mark
#     #Вывод полей
#     def info(self):
#         print(f'year: {self.year}')
#         print(f'mark: {self.mark}')
#
#     def __priceCar(self, price):
#         self.__price = price
#
# car = Car(2006, "BMW")
# car.info()

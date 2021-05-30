# Создайте класс Bus, унаследованный от класса Vehicle. Задайте аргументу
# capacity
# Bus.seating_capacity() значение по умолчанию 50
# Используйте следующий код для родительского класса Vehicle. Вам нужно использовать переопределение метода.
#
#
#

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# v = Vehicle('Man','150km',2500)
# v.seating_capacity()
# print(v.name,v.mileage,)
# print(v.seating_capacity())
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage,)
        self.seating_capacity(capacity=50)

    def seating_capacity(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


b = Bus('Mers', '200', 2500)
print(b.name, b.max_speed, b.mileage)
print(b.seating_capacity())

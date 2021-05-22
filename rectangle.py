# class  Rectangle
# Построить
# класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.).
#
# Класс
# должен содержать:
#
# Данные:
#
# длина и ширина прямоугольника
#
# Методы для операций с данными:
#
# Нахождения периметра, площади, изменения размеров, печати результата.
#
# Написать
# программу, демонстрирующую работу с этим классом. Программа должна содержать
# меню, позволяющее осуществить проверку всех методов класса.

# Прямоугольник
class Rectangle:
    '''это класс Rectangle'''
    # Cпособ создания  обьекта (констуктор)
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    #Метод расчета площади.
    def get_area(self):
        return self.width * self.height


# Создаем 2 объекта: rec1 & rec2
rec1 = Rectangle(10, 5)
rec2 = Rectangle(20, 11)
# Вывод
print("rec1.width = ", rec1.width)
print("rec1.width = ", rec1.height)
print("rec1.get_width() = ", rec1.get_width())
print("rec1.get_height() = ", rec1.get_height())


print("rec2.width = ", rec2.width)
print("rec2.height = ", rec2.height)
print("rec2.get_width() = ", rec2.get_width())
print("rec2.get_height() = ", rec2.get_height())

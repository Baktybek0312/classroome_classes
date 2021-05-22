# Класс Абонент
# Идентификационный номер, Фамилия, Имя, Отчество, Адрес, Номер кредитной карточки,
# Дебет, Кредит, Время междугородных и городских переговоров;
# Конструктор;
# Методы: установка значений атрибутов, получение значений атрибутов, вывод информации.
# Создать массив объектов данного класса.
# Вывести сведения относительно абонентов, у которых время городских переговоров превышает заданное.
# Сведения относительно абонентов, которые пользовались междугородной связью. Список абонентов в алфавитном порядке.

class Subscriber:
    def __init__(self, subs_id, last_name, first_name,
                 middle_name, address, credit_cart_number,
                 debit, credit, time_city_out, time_city_in):
        self.subs_id = subs_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.credit_cart_number = credit_cart_number
        self.debit = debit
        self.credit = credit
        self.time_city_out = time_city_out
        self.time_city_in = time_city_in

    def __str__(self):
        return f"{self.last_name} {self.first_name}, {self.subs_id}"


sub1 = Subscriber(1, 'Асанов', 'Бектур', 'Залкарович', 'Бишкек', 996880156592, 0, 1, 60, 15)
sub2 = Subscriber(2, 'Кутманов', 'Тумар', 'Тургунбаевич', 'Каракол', 996550188592, 1, 0, 60, 260)
sub3 = Subscriber(3, 'Айбеков', 'Бактияр', 'Куттубекович', 'Нарын', 996557188522, 0, 1, 120, 150)
sub4 = Subscriber(4, 'Кутманов', 'Тумар', 'Тургунбаевич', 'Кара-Балта', 996551188072, 1, 0, 60, 50)

sub_list = [sub1, sub2, sub3, sub4]

# def alf(subscriber):
#     return subscriber.last_name * subscriber.first_name
#
#
# result = sorted(sub_list, key=alf)
# print(result)

for subs in sub_list:
    if subs.time_city_in >= 200:
        print(subs, 'время городских переговоров превышает заданное')

    if subs.time_city_out > 0:
        print(subs, 'пользовались междугородной связью')



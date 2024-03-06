from abc import ABC, abstractmethod
from datetime import time
import time


class Mixin_Spicy:
    @staticmethod
    def attention():
        print("Это пицца острая!!!!!")


class Pizza(ABC):
    name = None

    def __init__(self, dough=None, sauce=None, filling=None, size=None):
        self.__dough = dough
        self.__sauce = sauce
        self.__filling = filling
        self.__size = size

    @abstractmethod
    def get_size(self):
        print(self.__size)
        pass



    def track_time(f):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = f(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Прошло {execution_time} секунд")
            return result
        return wrapper

    # Сравнение пицц по тесту
    def __eq__(self, other):
        if isinstance(other, Pizza):
            return self.__size == other.__size
        return False

    def __lt__(self, other):
        if isinstance(other, Pizza):
            return self.__size < other.__size
        return False

    @property
    def get_dough(self):
        return self.__dough

    @get_dough.setter
    def set_dough(self, dough):
        self.__dough = dough

    @property
    def get_sauce(self):
        return self.__sauce

    @get_sauce.setter
    def set_sauce(self, sauce):
        self.__sauce = sauce

    @property
    def get_filling(self):
        return self.__filling

    @get_filling.setter
    def set_filling(self, filling):
        self.__filling = filling

    @track_time
    def make_pizza(self):
        time.sleep(2)
        print(f"Замешено тесто для пиццы {self.name}")
        time.sleep(2)
        print("Подготовились ингредиенты")
        time.sleep(2)
        print("Пицца испеклась")
        time.sleep(1)
        print("Пицца нарезалась")
        time.sleep(1)
        print("Пицца упаковалась")



class BBQ_Pizza(Pizza, Mixin_Spicy):
    name = 'Барбекю'

    def __init__(self):
        super().__init__(dough="Thin", sauce="Soy", filling="Beef", size=25)

    def get_size(self):
            super().get_size()
            print('Вызван абстрактный метод в BBQ')


class Pepperoni(Pizza, Mixin_Spicy):
    name = 'Пепперони'

    def __init__(self):
        super().__init__(dough="Thick", sauce="Tomato sauce", filling="Pepperoni sausage", size=30)

    def get_size(self):
        super().get_size()
        print('Вызван абстрактный метод в Pepperoni')

class Seafood(Pizza):
    name = 'Дары моря'

    def __init__(self):
        super().__init__(dough="Medium", sauce="Cream sauce", filling="Squid", size=35)

    def get_size(self):
            super().get_size()
            print('Вызван абстрактный метод в Seafood')

class Terminal:
    menu = ['Перейти к меню', 'Просмотреть заказ', 'Отменить позицию', 'Завершить работу']
    menu_pizza = [Pepperoni, BBQ_Pizza, Seafood]
    sauces = ['Томатный', 'Сацебели', 'Тартар', 'Чесночный']
    doughs = ['Мучное', 'Рисовое', 'Хлебное']
    fillings = ['Пармезан', 'Томаты', 'Куриное филе', 'Грибы']

    def __init__(self):
        self.order = []

    @classmethod
    def show_menu_pizza(cls, menu_pizza):
        print('------------------------------')
        for i in range(len(menu_pizza)):
            print(f'{i + 1}.{menu_pizza[i].name}')
        print('------------------------------')

    @classmethod
    def show_sauces(cls):
        for i in range(len(cls.sauces)):
            print(f'{i + 1}.{cls.sauces[i]}')

    @classmethod
    def show_fillings(cls):
        for i in range(len(cls.fillings)):
            print(f'{i + 1}.{cls.fillings[i]}')

    @classmethod
    def show_dough(cls):
        for i in range(len(cls.doughs)):
            print(f'{i + 1}.{cls.doughs[i]}')

    def make_order(self, choose_pizza):
        self.order += [choose_pizza]

    def show_order(self):
        print('------------------------------')
        for i in range(len(self.order)):
            print(f"{i+1}.{self.order[i].name}")
            print(f" -Тесто: {self.order[i].get_dough}")
            print(f" -Соус: {self.order[i].get_sauce}")
            print(f" -Добавка: {self.order[i].get_filling}")
        print('------------------------------')

    def cancel_position(self):
        print('Выберите номер позиции для удаления: ')
        ans = int(input('>>> '))
        delete = self.order.pop(ans-1)
        print(f'Позиция {delete.name} удалена')

    def change_compound(self, choose_pizza_num):
        print('Хотите изменить состав пиццы?(+/-)')
        compound_ans = input('>>> ')
        choose_pizza = menu_pizza[choose_pizza_num - 1]()
        if compound_ans == '-':
            pass
        elif compound_ans == '+':
            print('Стандартная добавка: ')
            print(f"Тесто: {choose_pizza.get_dough}")
            print(f"Соус: {choose_pizza.get_sauce}")
            print(f"Добавка: {choose_pizza.get_filling}")
            print('Что хотите поменять?(соус, тесто, добавка)')
            ans_change_compound = input('>>> ')
            if ans_change_compound == 'соус':
                print('Доступные соусы: ')
                Terminal.show_sauces()
                new_sauce = input('>>> ')
                choose_pizza.set_sauce = new_sauce
            elif ans_change_compound == 'тесто':
                print('Доступное тесто: ')
                Terminal.show_dough()
                new_dough = input('>>> ')
                choose_pizza.set_dough = new_dough
            elif ans_change_compound == 'добавка':
                print('Доступные добавки: ')
                Terminal.show_fillings()
                new_fillings = input('>>> ')
                choose_pizza.set_fillings = new_fillings
        return choose_pizza


t1 = Terminal()
while True:
    menu = Terminal.menu
    menu_pizza = Terminal.menu_pizza
    print('Выберите действие: ')
    for i in range(len(menu)):
        print(f'{i + 1}.{menu[i]}')
    responce = input('>>> ')
    if responce == '1':
        Terminal.show_menu_pizza(menu_pizza)
        print('Выберите номер продукта: ')
        choose_pizza_num = int(input('>>> '))
        choose_pizza = t1.change_compound(choose_pizza_num)
        t1.make_order(choose_pizza)

    elif responce == '2':
        t1.show_order()
    elif responce == '3':
        t1.show_order()
        t1.cancel_position()
    elif responce == '4':
        print("Спасибо за заказ! Его уже начали готовить!")
        for i in t1.order:
            i.make_pizza()
        print('Ваши пиццы готовы! Приятного аппетита!')
        break

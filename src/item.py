import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __str__(self):
        return f'{self.__name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("../homework-2/items.csv", newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=",")
            for item in reader:
                cls.all.append(item)

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(self.__name) < 10:
            self.__name == name
        else:
            Exception("Длина наименования товара превышает 10 символов")

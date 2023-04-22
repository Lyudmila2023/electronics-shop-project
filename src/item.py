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
        # Item.all.append(self.name)

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
                name = item["name"]
                price = int(item["price"])
                quantity = int(item["quantity"])
                # exemp_class = name, price, quantity
                # print(exemp_class)
                cls.all.append(name)
            return name, price, quantity

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
            print("Exception: Длина наименования товара превышает 10 символов")





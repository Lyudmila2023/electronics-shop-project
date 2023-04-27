from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, sim_number):
        super().__init__(name, price, quantity)
        self.sim_number = sim_number

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim_number})"

    @property
    def number_of_sim(self):
        return self.sim_number

    @number_of_sim.setter
    def number_of_sim(self, sim_number):
        if sim_number == 0:
            raise "ValueError: Количество физических SIM-карт должно быть целым числом больше нуля."
        else:
            return self.sim_number


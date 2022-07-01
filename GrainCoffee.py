from CaffeineBeverage import CaffeineBeverage
from Coffee import Coffee


class GrainCoffee(Coffee, CaffeineBeverage):
    def __init__(self, name, price, color, medium_size, weight, caffeine_level):
        super().__init__(name, price, color)
        self.medium_size = medium_size
        self.weight = weight
        self.caffeine_level = caffeine_level

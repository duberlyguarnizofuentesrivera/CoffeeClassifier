from CaffeineBeverage import CaffeineBeverage
from Coffee import Coffee


class InstantCoffee(Coffee, CaffeineBeverage):
    def __init__(self, name, price, color, presentation, brand, caffeine_level):
        super().__init__(name, price, color)
        self.presentation = presentation
        self.brand = brand
        self.caffeine_level = caffeine_level

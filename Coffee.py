class Coffee:
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    def __str__(self):
        return "{} - {} @ ${}".format(self.name, self.color, self.price)

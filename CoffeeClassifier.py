import pickle


class CoffeeClassifier:

    def __init__(self):
        self.coffee_list = []

    def add_coffee(self, coffee):
        self.coffee_list.append(coffee)

    def remove_coffee(self, coffee):
        self.coffee_list.remove(coffee)

    def save_coffee_list(self):
        with open('coffee_list.pickle', 'wb') as f:
            pickle.dump(self.coffee_list, f)

    def load_coffee_list(self):
        with open('coffee_list.pickle', 'rb') as f:
            self.coffee_list = pickle.load(f)

    def get_coffee_list(self):
        return self.coffee_list

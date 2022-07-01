from flask import Flask, render_template, redirect

from CoffeeClassifier import CoffeeClassifier
from GrainCoffee import GrainCoffee
from InstantCoffee import InstantCoffee

app = Flask(__name__)
classifier = CoffeeClassifier()


@app.route('/')
def index():
    instant_coffee_list = []
    grain_coffee_list = []
    for coffee in classifier.get_coffee_list():
        if isinstance(coffee, InstantCoffee):
            instant_coffee_list.append(coffee)
        elif isinstance(coffee, GrainCoffee):
            grain_coffee_list.append(coffee)
    return render_template('index.html', instant_coffee_list=instant_coffee_list, grain_coffee_list=grain_coffee_list)


@app.route('/load_demo')
def load_demo_data():
    classifier.add_coffee(GrainCoffee('Cappuccino Alpino', 2.50, 'black', 'bag', 'small', 'medium'))
    classifier.add_coffee(GrainCoffee('Deluxe Shame', 3.50, 'green', 'medium', 'small', 'high'))
    classifier.add_coffee(GrainCoffee('Black Is The New Black', 2.60, 'black', 'medium', 'medium', 'medium'))
    classifier.add_coffee(InstantCoffee('Expensive means rich', 4.90, 'green', 'glass', 'El Colombiano', 'medium'))
    classifier.add_coffee(InstantCoffee('Mexican Coffee sold by USA', 3.50, 'black', 'bag', 'Café Y Canela', 'medium'))
    classifier.add_coffee(InstantCoffee('Contraband Nigerian Coffee', 4.50, 'green', 'glass', 'El Colombiano', 'low'))
    classifier.save_coffee_list()
    return redirect('/')


@app.route('/remove_coffee/<string:coffee_name>')
def remove_coffee(coffee_name):
    print("Removing coffee: " + coffee_name)
    for coffee in classifier.get_coffee_list():
        if coffee.name == coffee_name:
            classifier.remove_coffee(coffee)
            classifier.save_coffee_list()
            return redirect('/')
    return 'Coffee not found'


if __name__ == '__main__':
    app.run(debug=True)

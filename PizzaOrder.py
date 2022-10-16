#pizzaorder

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
class PizzaOrder:
    def __init__(self, time):
        self.pizzas = []
        self.time = time


    def getTime(self):
        return self.time

    def setTime(self, time):
        self.time = time

    def addPizza(self, pizza):
        self.pizzas.append(pizza)

    def getOrderDescription(self):
        output = ""
        output += "******\n"
        output += "Order Time: {}\n".format(self.time)
        total = 0
        for i in self.pizzas:
            output += i.getPizzaDetails() + "\n" + "----\n"
            total += i.getPrice()
        output += "TOTAL ORDER PRICE: ${:.2f}\n".format(total)
        output += "******\n"
        return output

#customPizza
from Pizza import Pizza

class CustomPizza(Pizza):

    def __init__(self, size):
        Pizza.__init__(self, size)
        self.toplist = []
        if self.size == "S":
            self.price += 8.00
        elif self.size == "M":
            self.price = 10.00
        elif self.size == "L":
            self.price = 12.00


    def addTopping(self, topping):
        self.toplist.append(topping)
        if self.size == "S" and len(self.toplist) != 0:
            self.price = 8.00 + (len(self.toplist)*0.5)
        elif self.size == "M" and len(self.toplist) != 0:
            self.price = 10.00 + (len(self.toplist)*0.75)
        elif self.size == "L" and len(self.toplist) != 0:
            self.price = 12.00 + len(self.toplist)


    def getPizzaDetails(self):
        output = ''
        output += "CUSTOM PIZZA\n"
        output += "Size: {}\n".format(self.size)
        output += "Toppings:\n"
        for i in self.toplist:
            output += "\t+ " + i + "\n"
        output += "Price: ${:.2f}\n".format(self.price)
        return output




# -*- coding:utf-8 -*-
import pytest
from Pizza import Pizza
from PizzaOrder import PizzaOrder
from OrderQueue import *
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza


def test_pizza():
    pizza = Pizza()
    pizza.setSize("S")
    pizza.setPrice(10)
    assert pizza.getPrice() == 10
    assert pizza.getSize() == "S"

def test_custom_pizza():
    cp1 = CustomPizza("S")
    assert cp1.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"
    cp2 = CustomPizza("L")
    cp2.addTopping("sausage")
    assert cp2.getPizzaDetails() == \
"CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ sausage\n\
Price: $13.00\n"

def test_specialty_pizza():
    sp = SpecialtyPizza("S", "Carne-more")
    assert sp.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
    sp = SpecialtyPizza("M", "Carne-more")
    assert sp.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: M\n\
Name: Carne-more\n\
Price: $14.00\n"

def test_pizza_order():
    cp1 = CustomPizza("S")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000)  # 12:30:00PM order.addPizza(cp1)
    order.addPizza(cp1)
    order.addPizza(sp1)
    assert order.getOrderDescription() == \
"******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ sausage\n\
Price: $8.50\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $20.50\n\
******\n"

    cp1.addTopping("extra cheese")
    order.setTime("134505")
    assert order.getOrderDescription() == \
"******\n\
Order Time: 134505\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ sausage\n\
\t+ extra cheese\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"

def test_order_queue():
    oq = OrderQueue()
    sp1 = SpecialtyPizza("S", "Carne-more")
    po1 = PizzaOrder(123000)  # 12:30:00PM order.addPizza(cp1)
    po1.addPizza(sp1)

    sp2 = SpecialtyPizza("M", "Shrimpsss")
    po2 = PizzaOrder(123100)
    po2.addPizza(sp2)

    sp3 = SpecialtyPizza("L", "Shrimpsss")
    po3 = PizzaOrder(122900)
    po3.addPizza(sp3)

    oq.addOrder(po1)
    oq.addOrder(po2)
    oq.addOrder(po3)

    assert oq.processNextOrder() == po3.getOrderDescription()
    assert oq.processNextOrder() == po1.getOrderDescription()
    assert oq.processNextOrder() == po2.getOrderDescription()

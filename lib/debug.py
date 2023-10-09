#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
   
    coffee = Coffee("Mocha")
    customer = Customer('Steve')
    order_1 = Order(customer, coffee, 2)
    order_2 = Order(customer, coffee, 5)

    coffee_2 = Coffee("latte")
    order_3 = Order(customer, coffee_2, 4)
    order_4 = Order(customer, coffee_2, 6)


    ipdb.set_trace()

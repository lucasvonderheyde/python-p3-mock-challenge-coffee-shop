
class Order:

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.customer.orders.append(self)
        self.coffee.orders.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):

        if new_price > 1 and new_price < 11:

            self._price = new_price
        
        else:
            print("gotta be some other price man")

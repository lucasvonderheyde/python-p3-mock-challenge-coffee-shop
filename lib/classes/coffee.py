class Coffee:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def get_customers(self):
        customers = []
        for order in self.orders:
            customers.append(order.customer)
        return customers
    
    def num_orders(self):
        return len(self.orders)
    
    def average_price(self):
        avg_price = 0
        for order in self.orders:
            avg_price += order.price
        return avg_price/len(self.orders)

    # @property
    # def name(self):
    #     return self._name
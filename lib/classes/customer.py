class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []
    
    def get_coffees(self):
        customer_coffees = []
        for order in self.orders:
            customer_coffees.append(order.coffee)
        return customer_coffees

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        
        if len(new_name) > 1 and len(new_name) < 16:
            self._name = new_name
        
        else:
            print("name must be between some charcter count")
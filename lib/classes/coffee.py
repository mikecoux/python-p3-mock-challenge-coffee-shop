class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

    """name property"""
    def get_name(self):
        return self._name
    def set_name(self, name):
        if not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
    name = property(get_name, set_name)

    """instance methods"""
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        return len(self._orders)
    
    def average_price(self):
        return sum([order.price for order in self._orders]) \
        / len(self._orders)
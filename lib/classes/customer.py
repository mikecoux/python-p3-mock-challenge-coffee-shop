class Customer:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []

    """name property"""
    # @property
    def get_name(self):
        return self._name
    # @get_name.setter
    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) <= 15:
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
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        return set(self._coffees)
    
    def create_order(self, coffee, price):
        from classes.order import Order
        return Order(self, coffee, price)
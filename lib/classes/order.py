from classes.customer import Customer
from classes.coffee import Coffee
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        """send data methods"""
        coffee.orders(self)
        coffee.customers(customer)
        customer.orders(self)
        customer.coffees(coffee)
        """append to all"""
        Order.all.append(self)
    
    """price property"""
    # @property
    def get_price(self):
        return self._price
    # @get_price.setter
    def set_price(self, price):
        if isinstance(price, int) and 0 < price <= 10:
            self._price = price
        else:
            raise Exception
    price = property(get_price, set_price)

    """customer property"""
    def get_customer(self):
        return self._customer
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
    customer = property(get_customer, set_customer)

    """coffee property"""
    def get_coffee(self):
        return self._coffee
    def set_coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception
    coffee = property(get_coffee, set_coffee)
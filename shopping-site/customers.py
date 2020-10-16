"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first, last, email, password):
        """Initializes Customer"""

        self.first = first
        self.last = last
        self.email = email
        self.password = password

    def __repr__(self):
        """Convenience method to show information about Customer in console."""
        
        return "<Customer: {} {}>".format(self.first, self.last)


def read_customer_types_from_file(filepath):
    """Read customer data and populate dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    customers = {}

    with open(filepath) as file:
        for line in file:
            (first, last, email, password) = line.strip().split("|")

            customers[email] = Customer(first, last, email, password)

    return customers


def get_by_email(email):
    """Return a customer, given its email."""

    return customers[email]

    
customers = read_customer_types_from_file('customers.txt')
 
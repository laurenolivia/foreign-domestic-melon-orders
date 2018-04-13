"""Classes for melon orders."""

class AbstractOrder(object):
    """ Abstract base class that other orders inherit from. """

    def __init__(self, species, qty):
        """ Initialize melon order attributes across all orders. """
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code

    #if qty < 10:
        self.total = original total + 3
    else:
        return total         

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


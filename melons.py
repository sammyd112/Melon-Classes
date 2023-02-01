"""Classes for melon orders."""

class AbstractMelonOrder: #superclass
    """An abstract base class that other Melon Orders inherit from."""
    tax = 0.00
    

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.species = species
        self.qty = qty
        # self.tax = tax
        # self.shipped = shipped
        # self.order_type = order_type
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5

        if self.species == "christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        # if self.order_type == "international" and self.qty < 10:
        #      total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder): #subclass
    """A melon order within the USA."""
    tax = 0.08
    order_type = "domestic"

    # def __init__(self, species, qty,): 
    #     """Initialize melon order attributes."""
    #     super().__init__(species, qty)
        # self.shipped = False <-- doesn't matter


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international" # <-- subclass attributes

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

        # self.shipped = False 
    def get_total(self):
        total = super().get_total() 
        if self.qty < 10:
            total += 3
        
        return total
        

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """no tax, """

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = passed
        return self.passed_inspection
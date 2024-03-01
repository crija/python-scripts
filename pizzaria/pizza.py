PIZZA_VALUE = {'P': 34.99, 'M': 42.99, 'G': 55.99}
LIST_ADDITIONALS = {'cheddar': 4.25, 'maionese verde': 2.50, 'morango': 5.15, 'chocolate preto': 8.90}
LIST_EDGE = {'catupiry': 10.99, 'bombom': 15.90}

class Pizza:
    def __init__(self, size, flavors, edge, chosen_additional):
        self.size = size
        self.flavors = flavors
        self.edge = edge
        self.chosen_additional = chosen_additional

    def calculate_value(self):
        size_value = PIZZA_VALUE[self.size]
        additional_value = LIST_ADDITIONALS.get(self.chosen_additional, 0)
        edge_value = LIST_EDGE.get(self.edge, 0)
        return sum([size_value, additional_value, edge_value])
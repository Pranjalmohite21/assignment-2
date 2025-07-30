class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.items.append({'name': name, 'price': price})

    def total_cost(self):
        return sum(item['price'] for item in self.items)

import math


class Position:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def distance_to(self, other):
        return math.ceil(math.sqrt((self.row - other.row) ** 2 + (self.col - other.col) ** 2))

    def __eq__(self, other):
        return isinstance(other, Position) and self.row == other.row and self.col == other.col

    def __hash__(self):
        return hash((self.row, self.col))

    def __repr__(self):
        return f"({self.row},{self.col})"


class Product:
    def __init__(self, id, weight):
        self.id = id
        self.weight = weight

    def __repr__(self):
        return f"P{self.id}(w={self.weight})"


class Warehouse:
    def __init__(self, id, position, inventory):
        self.id = id
        self.position = position
        self.inventory = dict(inventory)

    def has_product(self, product_id, quantity=1):
        return self.inventory.get(product_id, 0) >= quantity

    def remove_product(self, product_id, quantity=1):
        if not self.has_product(product_id, quantity):
            raise ValueError(f"warehouse {self.id} missing product {product_id}")
        self.inventory[product_id] -= quantity

    def add_product(self, product_id, quantity=1):
        self.inventory[product_id] = self.inventory.get(product_id, 0) + quantity

    def __repr__(self):
        return f"W{self.id}@{self.position}"


class Order:
    def __init__(self, id, position, items):
        self.id = id
        self.position = position
        self.items = list(items)
        self._delivered = {}

    def need(self, product_id):
        needed = self.items.count(product_id)
        return needed - self._delivered.get(product_id, 0)

    def deliver(self, product_id):
        if self.need(product_id) <= 0:
            raise ValueError(f"order {self.id} doesn't need product {product_id}")
        self._delivered[product_id] = self._delivered.get(product_id, 0) + 1

    def is_complete(self):
        return all(self.need(pid) <= 0 for pid in set(self.items))

    def pending_items(self):
        result = []
        for pid in set(self.items):
            n = self.need(pid)
            if n > 0:
                result.extend([pid] * n)
        return result

    def __repr__(self):
        return f"O{self.id}@{self.position}"

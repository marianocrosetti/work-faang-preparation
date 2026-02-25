from models import Position


class Drone:
    def __init__(self, id, position, max_payload):
        self.id = id
        self.position = Position(position.row, position.col)
        self.max_payload = max_payload
        self.carried = {}
        self.busy_until = 0

    def current_load(self, products):
        return sum(products[pid].weight * qty for pid, qty in self.carried.items())

    def can_carry(self, product_id, quantity, products):
        additional = products[product_id].weight * quantity
        return self.current_load(products) + additional <= self.max_payload

    def load(self, product_id, quantity):
        self.carried[product_id] = self.carried.get(product_id, 0) + quantity

    def unload(self, product_id, quantity):
        current = self.carried.get(product_id, 0)
        if current < quantity:
            raise ValueError(f"drone {self.id} carries only {current} of product {product_id}")
        self.carried[product_id] -= quantity
        if self.carried[product_id] == 0:
            del self.carried[product_id]

    def is_free(self, turn):
        return turn >= self.busy_until

    def __repr__(self):
        return f"Drone{self.id}@{self.position}"

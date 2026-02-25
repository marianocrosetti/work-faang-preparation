from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def describe(self):
        pass

    def __repr__(self):
        return self.describe()


class Load(Command):
    def __init__(self, drone_id, warehouse_id, product_id, quantity=1):
        self.drone_id = drone_id
        self.warehouse_id = warehouse_id
        self.product_id = product_id
        self.quantity = quantity

    def describe(self):
        return f"D{self.drone_id} LOAD W{self.warehouse_id} P{self.product_id} x{self.quantity}"


class Deliver(Command):
    def __init__(self, drone_id, order_id, product_id, quantity=1):
        self.drone_id = drone_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def describe(self):
        return f"D{self.drone_id} DELIVER O{self.order_id} P{self.product_id} x{self.quantity}"


class Wait(Command):
    def __init__(self, drone_id, turns):
        self.drone_id = drone_id
        self.turns = turns

    def describe(self):
        return f"D{self.drone_id} WAIT {self.turns}"

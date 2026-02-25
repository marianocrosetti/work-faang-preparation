from models import Position, Product, Warehouse, Order
from drone import Drone


class World:
    def __init__(self, rows, cols, num_drones, max_payload, max_turns, products, warehouses, orders):
        self.rows = rows
        self.cols = cols
        self.num_drones = num_drones
        self.max_payload = max_payload
        self.max_turns = max_turns
        self.products = {p.id: p for p in products}
        self.warehouses = {w.id: w for w in warehouses}
        self.orders = {o.id: o for o in orders}

    def create_drones(self):
        start = self.warehouses[0].position
        return [Drone(i, start, self.max_payload) for i in range(self.num_drones)]

    @staticmethod
    def from_dict(d):
        products = [Product(i, w) for i, w in enumerate(d["product_weights"])]
        warehouses = [
            Warehouse(i, Position(w["row"], w["col"]), w["inventory"])
            for i, w in enumerate(d["warehouses"])
        ]
        orders = [
            Order(i, Position(o["row"], o["col"]), o["items"])
            for i, o in enumerate(d["orders"])
        ]
        return World(
            d["rows"], d["cols"], d["num_drones"], d["max_payload"],
            d["max_turns"], products, warehouses, orders,
        )

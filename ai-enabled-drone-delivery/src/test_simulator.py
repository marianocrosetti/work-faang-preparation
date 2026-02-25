import unittest
from models import Position, Product, Warehouse, Order
from commands import Load, Deliver, Wait
from drone import Drone
from world import World
from simulator import Simulator


def make_world(overrides=None):
    base = {
        "rows": 10, "cols": 10,
        "num_drones": 1, "max_payload": 50, "max_turns": 30,
        "product_weights": [10, 20, 5],
        "warehouses": [
            {"row": 0, "col": 0, "inventory": {0: 5, 1: 3, 2: 10}},
        ],
        "orders": [
            {"row": 3, "col": 3, "items": [0]},
            {"row": 5, "col": 4, "items": [1]},
        ],
    }
    if overrides:
        base.update(overrides)
    return World.from_dict(base)


class TestModels(unittest.TestCase):

    def test_distance_same_point(self):
        a = Position(5, 5)
        self.assertEqual(a.distance_to(a), 0)

    def test_distance_horizontal(self):
        a, b = Position(0, 0), Position(0, 3)
        self.assertEqual(a.distance_to(b), 3)

    def test_distance_diagonal(self):
        a, b = Position(0, 0), Position(3, 4)
        self.assertEqual(a.distance_to(b), 5)

    def test_distance_rounds_up(self):
        a, b = Position(0, 0), Position(1, 1)
        self.assertEqual(a.distance_to(b), 2)

    def test_warehouse_inventory(self):
        wh = Warehouse(0, Position(0, 0), {0: 3, 1: 1})
        self.assertTrue(wh.has_product(0, 2))
        wh.remove_product(0, 2)
        self.assertTrue(wh.has_product(0, 1))
        self.assertFalse(wh.has_product(0, 2))

    def test_warehouse_remove_missing_raises(self):
        wh = Warehouse(0, Position(0, 0), {0: 1})
        with self.assertRaises(ValueError):
            wh.remove_product(1)

    def test_order_completion(self):
        order = Order(0, Position(5, 5), [0, 0, 1])
        self.assertFalse(order.is_complete())
        order.deliver(0)
        order.deliver(0)
        self.assertFalse(order.is_complete())
        order.deliver(1)
        self.assertTrue(order.is_complete())

    def test_order_over_deliver_raises(self):
        order = Order(0, Position(5, 5), [0])
        order.deliver(0)
        with self.assertRaises(ValueError):
            order.deliver(0)


class TestDrone(unittest.TestCase):

    def test_load_and_weight(self):
        products = {0: Product(0, 10), 1: Product(1, 20)}
        drone = Drone(0, Position(0, 0), 50)
        drone.load(0, 2)
        self.assertEqual(drone.current_load(products), 20)

    def test_can_carry_check(self):
        products = {0: Product(0, 30)}
        drone = Drone(0, Position(0, 0), 50)
        self.assertTrue(drone.can_carry(0, 1, products))
        drone.load(0, 1)
        self.assertFalse(drone.can_carry(0, 1, products))

    def test_unload_missing_raises(self):
        drone = Drone(0, Position(0, 0), 50)
        with self.assertRaises(ValueError):
            drone.unload(0, 1)


class TestSimulator(unittest.TestCase):

    def test_single_delivery(self):
        world = make_world()
        commands = [
            Load(0, 0, 0),
            Deliver(0, 0, 0),
        ]
        result = Simulator(world).run(commands)
        self.assertEqual(result.completed, 1)
        self.assertTrue(result.on_time)

    def test_two_deliveries_sequential(self):
        world = make_world()
        commands = [
            Load(0, 0, 0),
            Load(0, 0, 1),
            Deliver(0, 0, 0),
            Deliver(0, 1, 1),
        ]
        result = Simulator(world).run(commands)
        self.assertEqual(result.completed, 2)
        self.assertTrue(result.all_completed)

    def test_wait_command(self):
        world = make_world()
        commands = [
            Wait(0, 5),
            Load(0, 0, 0),
            Deliver(0, 0, 0),
        ]
        result = Simulator(world).run(commands)
        self.assertEqual(result.completed, 1)
        # wait 5 + load 1 + travel 5 + deliver 1 = 12
        self.assertEqual(result.max_turn, 12)

    def test_unknown_command_raises(self):
        world = make_world()

        class FakeCmd:
            drone_id = 0
        with self.assertRaises(Exception):
            Simulator(world).run([FakeCmd()])

    def test_score_calculation(self):
        world = make_world()  # max_turns=30
        commands = [
            Load(0, 0, 0),
            Deliver(0, 0, 0),
        ]
        result = Simulator(world).run(commands)
        # drone starts at (0,0), load at W0(0,0): 0 travel + 1 = turn 1
        # deliver to O0(3,3): ceil(sqrt(18))=5 travel + 1 = turn 7
        # score = ceil((30 - 7) / 30 * 100) = ceil(76.67) = 77
        self.assertEqual(result.score, 77)

    def test_overloaded_drone_rejected(self):
        world = make_world({"product_weights": [20]})  # payload=50
        commands = [
            Load(0, 0, 0, 3),  # 3 x 20 = 60 > 50
        ]
        with self.assertRaises(Exception):
            Simulator(world).run(commands)

    # ???? uncomment and implement the Move command
    # def test_move_command(self):
    #     world = make_world()
    #     from commands import Move
    #     commands = [
    #         Move(0, Position(5, 5)),
    #         Load(0, 0, 0),
    #         Deliver(0, 0, 0),
    #     ]
    #     result = Simulator(world).run(commands)
    #     # move to (5,5): ceil(sqrt(50))=8 turns (no +1, just travel)
    #     # load at W0(0,0): travel 8 + 1 = 9
    #     # deliver to O0(3,3): travel 5 + 1 = 6
    #     # total: 8 + 9 + 6 = 23
    #     self.assertEqual(result.max_turn, 23)
    #     self.assertTrue(result.on_time)


if __name__ == "__main__":
    unittest.main()

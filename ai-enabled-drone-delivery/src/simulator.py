import math
from copy import deepcopy
from commands import Command, Load, Deliver, Wait
from world import World


class SimulationError(Exception):
    pass


class SimulationResult:
    def __init__(self, score, completed, total_orders, max_turn, max_turns):
        self.score = score
        self.completed = completed
        self.total_orders = total_orders
        self.max_turn = max_turn
        self.max_turns = max_turns

    @property
    def all_completed(self):
        return self.completed == self.total_orders

    @property
    def on_time(self):
        return self.max_turn <= self.max_turns

    def __repr__(self):
        return (
            f"Score: {self.score} | "
            f"Orders: {self.completed}/{self.total_orders} | "
            f"Turns: {self.max_turn}/{self.max_turns}"
        )


class Simulator:
    def __init__(self, world):
        self.original_world = world
        self.world = None
        self.drones = None
        self.completed_orders = {}

    def run(self, commands):
        self.world = deepcopy(self.original_world)
        self.drones = self.world.create_drones()
        self.completed_orders = {}

        for cmd in commands:
            self._execute(cmd)

        return self._build_result()

    def _execute(self, cmd):
        drone = self.drones[cmd.drone_id]

        if isinstance(cmd, Load):
            wh = self.world.warehouses[cmd.warehouse_id]
            travel = drone.position.distance_to(wh.position)
            drone.busy_until += travel + 1
            drone.position = wh.position

            wh.remove_product(cmd.product_id, cmd.quantity)
            drone.load(cmd.product_id, cmd.quantity)

        elif isinstance(cmd, Deliver):
            order = self.world.orders[cmd.order_id]
            travel = drone.position.distance_to(order.position)
            drone.busy_until += travel + 1
            drone.position = order.position

            drone.unload(cmd.product_id, cmd.quantity)
            for _ in range(cmd.quantity):
                order.deliver(cmd.product_id)

            if order.is_complete() and order.id not in self.completed_orders:
                self.completed_orders[order.id] = drone.busy_until

        elif isinstance(cmd, Wait):
            drone.busy_until += cmd.turns

        else:
            raise SimulationError(f"unknown command: {cmd}")

    def _calculate_score(self):
        T = self.world.max_turns
        score = 0
        for order_id, turn in self.completed_orders.items():
            score += math.floor((T - turn) / T * 100)
        return score

    def _build_result(self):
        return SimulationResult(
            score=self._calculate_score(),
            completed=len(self.completed_orders),
            total_orders=len(self.world.orders),
            max_turn=max((d.busy_until for d in self.drones), default=0),
            max_turns=self.world.max_turns,
        )

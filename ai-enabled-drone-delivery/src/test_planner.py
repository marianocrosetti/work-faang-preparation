import unittest
from world import World
from simulator import Simulator
from planner import Planner
from scenarios import TINY, SMALL


class TestPlanner(unittest.TestCase):

    def test_planner_returns_commands(self):
        world = World.from_dict(TINY)
        planner = Planner(world)
        commands = planner.plan()
        # uncomment when Planner is implemented:
        # self.assertGreater(len(commands), 0)

    # def test_planner_completes_tiny(self):
    #     world = World.from_dict(TINY)
    #     planner = Planner(world)
    #     commands = planner.plan()
    #     result = Simulator(world).run(commands)
    #     self.assertTrue(result.all_completed, f"not all orders completed: {result}")
    #     self.assertTrue(result.on_time, f"exceeded max turns: {result}")

    # def test_planner_completes_small(self):
    #     world = World.from_dict(SMALL)
    #     planner = Planner(world)
    #     commands = planner.plan()
    #     result = Simulator(world).run(commands)
    #     self.assertTrue(result.all_completed, f"not all orders completed: {result}")
    #     self.assertTrue(result.on_time, f"exceeded max turns: {result}")

    # def test_planner_score_above_150(self):
    #     world = World.from_dict(SMALL)
    #     planner = Planner(world)
    #     commands = planner.plan()
    #     result = Simulator(world).run(commands)
    #     self.assertGreater(result.score, 150, f"score too low: {result}")


if __name__ == "__main__":
    unittest.main()

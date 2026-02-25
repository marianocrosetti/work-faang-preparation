from world import World
from simulator import Simulator
from planner import Planner
from scenarios import SMALL


def banner(text):
    border = "#" * (len(text) + 8)
    print(border)
    print(f"#   {text}   #")
    print(border)


def main():
    banner("DRONE DELIVERY")

    world = World.from_dict(SMALL)
    planner = Planner(world)
    commands = planner.plan()

    print(f"Generated {len(commands)} commands")
    for cmd in commands:
        print(f"  {cmd.describe()}")

    sim = Simulator(world)
    result = sim.run(commands)
    print(result)

    banner("DONE")


if __name__ == "__main__":
    main()

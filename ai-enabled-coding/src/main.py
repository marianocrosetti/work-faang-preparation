"""
Runs your Solver. It's useful to see how Solver is called.
You may want to change how Solver is constructed.
"""

from puzzle import Puzzle
from solver import Solver


def banner(legend: str) -> None:
    """Print a banner with the given legend text."""
    # workaround for all the build noise
    border = "#" * (len(legend) + 8)
    print(border)
    print(f"#   {legend}   #")
    print(border)


def main() -> None:
    """Main entry point for the wordlesolver."""
    banner("BEGIN CODE OUTPUT")

    puzzle = Puzzle("hard")
    solver = Solver(puzzle)
    solver.solve_puzzle()

    for guess in solver.get_guesses():
        print(guess)
    if puzzle.won():
        print(f"WIN in {puzzle.num_guesses()}!")
    else:
        print(f"LOSS! It was '{puzzle.admit_defeat()}'")
    banner("END CODE OUTPUT")


if __name__ == "__main__":
    main()

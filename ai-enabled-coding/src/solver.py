"""You'll implement this."""

from typing import List

from puzzle import Puzzle


class Solver:
    """Solves Wordle-style puzzles."""

    def __init__(self, puzzle: Puzzle):
        self.puzzle = puzzle
        self.guesses: List[str] = []

    def solve_puzzle(self) -> None:
        pass

    def get_guesses(self) -> List[str]:
        return self.guesses

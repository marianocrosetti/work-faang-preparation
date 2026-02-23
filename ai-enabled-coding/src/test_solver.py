"""Tests for Solver. Outlines for optional tests, maybe useful after Solver is functioning."""

import unittest

from puzzle import Puzzle
from solver import Solver


class SolverTest(unittest.TestCase):
    """Unit tests for the Solver class."""

    def test_should_solve_simple_case(self) -> None:
        """Test that the solver can solve a simple case."""
        puzzle = Puzzle("easy")
        solver = Solver(puzzle)
        solver.solve_puzzle()
        # Uncomment these assertions once Solver is implemented:
        # self.assertTrue(puzzle.won(), "couldn't guess 'easy'")
        # self.assertEqual(
        #     len(solver.get_guesses()),
        #     puzzle.num_guesses(),
        #     "don't cheat!"
        # )
        # self.assertLess(puzzle.num_guesses(), 7, "don't guess too much")

    # def test_should_be_an_optimal_guesser(self) -> None:
    #     """Test that the solver is optimized enough."""
    #     average_guesses = 10.0
    #     self.assertLess(average_guesses, 4.0, "not optimized enough")


if __name__ == "__main__":
    unittest.main()

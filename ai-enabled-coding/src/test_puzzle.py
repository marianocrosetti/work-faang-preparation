"""Tests for Puzzle. All of this is just boilerplate to make test cases compact and understandable."""

import unittest
from typing import List

from puzzle import Match, Puzzle


class TestCase:
    """Represents a test case for the puzzle."""

    def __init__(self, answer: str, guess: str, expected: str):
        self.answer = answer
        self.guess = guess
        self.expected = expected


class PuzzleTest(unittest.TestCase):
    """Unit tests for the Puzzle class."""

    def test_check(self) -> None:
        """Test the puzzle checking logic."""
        # Test cases:     answer, guess, expected result
        all_cases = [
            TestCase("dock", "dock", "YYYY"),
            TestCase("dock", "drop", "YNMN"),
            TestCase("dock", "dome", "YYNN"),
            TestCase("dock", "abcd", "not a word"),
            # TestCase("dock", "doff", "????"),
            # TestCase("dock", "dodo", "????"),
        ]

        failures = []
        for test_case in all_cases:
            puzzle = Puzzle(test_case.answer)
            try:
                actual = puzzle.guess(test_case.guess)
                actual_str = self._match_list_to_string(actual)
            except ValueError as e:
                actual_str = str(e)

            if test_case.expected != actual_str:
                failures.append(
                    f"answer={test_case.answer}, guess={test_case.guess}, "
                    f"got {actual_str} instead of {test_case.expected}"
                )

        if failures:
            self.fail(
                "\n=== TEST CASE FAILURES ===\n" + "\n".join(failures) + "\n=== END ==="
            )

    def _match_list_to_string(self, matches: List[Match]) -> str:
        """Convert a list of Match results to a string representation."""
        result = []
        for match in matches:
            if match == Match.YES:
                result.append("Y")
            elif match == Match.MOVE:
                result.append("M")
            else:  # Match.NO
                result.append("N")
        return "".join(result)


if __name__ == "__main__":
    unittest.main()

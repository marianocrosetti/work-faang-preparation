"""Read this first."""

from enum import Enum
from typing import List

from dictionary import get_prod_dictionary, get_test_dictionary


class Match(Enum):
    YES = "YES"
    NO = "NO"
    MOVE = "MOVE"


class Puzzle:
    def __init__(self, answer: str):
        self.answer = list(answer.lower())
        self.eligible_words = get_prod_dictionary()
        self._won = False
        self._lost = False
        self._num_guesses = 0

    def answer_length(self) -> int:
        return len(self.answer)

    def _check_guess(self, guess: str) -> List[Match]:
        guess_chars = list(guess)
        result = [Match.NO] * len(self.answer)

        for idx in range(len(self.answer)):
            if guess_chars[idx] == self.answer[idx]:
                result[idx] = Match.YES
            else:
                for other_idx in range(len(self.answer)):
                    if guess_chars[idx] == self.answer[other_idx]:
                        result[idx] = Match.MOVE
                        break

        return result

    def guess(self, guess: str) -> List[Match]:
        if self._lost:
            raise RuntimeError("game over")
        if len(guess) != len(self.answer):
            raise ValueError("wrong length")
        if guess not in self.eligible_words:
            raise ValueError("not a word")

        result = self._check_guess(guess)

        if all(match == Match.YES for match in result):
            self._won = True
        self._num_guesses += 1
        return result

    def won(self) -> bool:
        return self._won

    def num_guesses(self) -> int:
        return self._num_guesses

    def admit_defeat(self) -> str:
        self._lost = True
        return "".join(self.answer)

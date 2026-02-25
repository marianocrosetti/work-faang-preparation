# My journey

- Read and understand
- List all the test cases that are failing NOT BECAUSE "Not Implemented"
- Fix them
- List all the test cases that are failing because "Not Implemented"
- Optimize the algorithm
    - Current implementation:
        - List all the methods + their complexities
        - For not implemented I will try to do my best
    - Efficient implementation:



# Prompts
❯ Read the src files and give me a concise schema of the classes and how they compose and what they do

Double check the tests `TEST_NAME_HERE` and make me a list of possible drawbacks

# Class diagram

  Class Diagram

  Dictionary (module)
    └─ provides word sets (test/prod) via get_test_dictionary() / get_prod_dictionary()

  Match (Enum)
    YES   — correct letter, correct position (green)
    NO    — letter not in answer
    MOVE  — correct letter, wrong position (yellow)

  Puzzle
    ├─ answer: List[char]
    ├─ eligible_words: Set[str]   ← from dictionary
    ├─ guess(str) → List[Match]   — validates & scores a guess
    ├─ won() → bool
    ├─ num_guesses() → int
    └─ admit_defeat() → str       — reveals answer, locks game

  Solver
    ├─ puzzle: Puzzle              ← composition
    ├─ guesses: List[str]
    ├─ solve_puzzle() → None       — **stub, not yet implemented**
    └─ get_guesses() → List[str]

  How they compose

  Dictionary feeds word sets into Puzzle. Puzzle is the game engine — it holds the secret answer, validates guesses against the dictionary, and returns Match results
  per character. Solver receives a Puzzle instance and is expected to call puzzle.guess() repeatedly, accumulating guesses until puzzle.won(). Main wires them together:
   creates a Puzzle with a secret word, passes it to Solver, runs solve_puzzle(), then prints results.

  The task is to implement Solver.solve_puzzle() — it's currently a pass.
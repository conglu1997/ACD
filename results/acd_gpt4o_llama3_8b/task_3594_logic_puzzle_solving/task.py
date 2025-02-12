class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "sudoku", "puzzle": "530070000600195000098000060800060003400803001700020006060000280000419005000080079"},
            "2": {"type": "crossword", "clues": {
                "Across": {"1": "A fruit (6 letters)", "4": "A color (3 letters)"},
                "Down": {"1": "A type of tree (3 letters)", "2": "An animal (4 letters)"}
            }, "grid": [
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " "]
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "sudoku":
            return f"""Solve the following Sudoku puzzle. The puzzle is given as a single string of 81 characters where '0' represents an empty cell. Submit your solution as a single string of 81 characters, representing the completed puzzle. Ensure that each row, column, and 3x3 subgrid contains all digits from 1 to 9.

Puzzle: {t['puzzle']}"""
        elif t["type"] == "crossword":
            clues = t['clues']
            return f"""Solve the following crossword puzzle. Fill in the grid based on the provided clues. Submit your solution as a 6x6 grid, with each cell containing a single letter, in plain text format.

Clues:
Across:
1. {clues['Across']['1']} (Starts at 1,1)
4. {clues['Across']['4']} (Starts at 2,1)

Down:
1. {clues['Down']['1']} (Starts at 1,1)
2. {clues['Down']['2']} (Starts at 2,4)

Example submission format (replace X with your answers):
XX XX
XX XX
XX XX
XX XX
XX XX
XX XX
"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "sudoku":
            criteria = ["The solution must be a valid completed Sudoku grid, with each row, column, and 3x3 subgrid containing all digits from 1 to 9."]
        elif t["type"] == "crossword":
            criteria = ["The solution must be a valid filled crossword grid, matching the given clues in both Across and Down directions."]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

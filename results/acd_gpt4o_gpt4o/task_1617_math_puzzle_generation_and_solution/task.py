class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Create a 4x4 Sudoku puzzle with a unique solution. Each row, column, and 2x2 subgrid must contain all digits from 1 to 4.", "puzzle": "1___ 2___ __3_ ____"},
            "2": {"constraints": "Create a 3x3 magic square. The sum of the numbers in each row, column, and diagonal must be the same.", "puzzle": "8__ 3_7 4_2"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is twofold: first, generate a mathematical puzzle based on the given constraints; second, solve the provided puzzle.

Constraints for puzzle generation: {t['constraints']}

Provide your generated puzzle and solution in the format 'Generated Puzzle: [your puzzle], Solution: [your solution]'.

Here is a puzzle for you to solve:

Puzzle: {t['puzzle']}

Provide your solution to the puzzle in plain text format. Ensure both your generated puzzle and the provided puzzle are solved correctly. For the provided puzzle, write 'Solution: [your solution]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

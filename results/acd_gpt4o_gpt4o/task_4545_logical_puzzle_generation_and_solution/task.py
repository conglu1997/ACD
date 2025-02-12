class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": ["The puzzle should involve a 4x4 grid.", "Each row, column, and diagonal should sum to 34.", "It should use numbers 1 to 16 exactly once."]},
            "2": {"constraints": ["The puzzle should involve a sequence of letters.", "It should form a valid word or phrase when solved.", "Each letter should be used exactly once."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a logical puzzle based on the following constraints and provide a step-by-step solution to solve it:

Constraints: {', '.join(t['constraints'])}

Ensure that the puzzle is logical, coherent, and solvable. The instructions should be clear and easy to follow, and the solution should be detailed and correct. Provide your response in the following format:

Puzzle: [Your puzzle description]
Solution: [Step-by-step solution]

Example:
Puzzle: Fill the 4x4 grid with numbers 1 to 16 such that each row, column, and diagonal sums to 34. The grid should be aligned as follows:
_ _ _ _
_ _ _ _
_ _ _ _
_ _ _ _
Solution:
1. Place 1 in the top-left cell.
2. Place 15 in the top-middle-left cell.
3. Place 14 in the top-middle-right cell.
4. Place 4 in the top-right cell.
5. Place 12 in the middle-top-left cell.
6. Place 6 in the center cell.
7. Place 7 in the middle-bottom-left cell.
8. Place 9 in the middle-bottom-right cell.
9. Place 8 in the bottom-left cell.
10. Place 5 in the bottom-middle-left cell.
11. Place 10 in the bottom-middle-right cell.
12. Place 11 in the bottom-right cell.
13. Place 2 in the middle-top-right cell.
14. Place 13 in the middle-bottom-right cell.
15. Place 3 in the center-left cell.
16. Place 16 in the center-right cell."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The puzzle should meet the given constraints.", "The puzzle should be logical and coherent.", "The solution should be detailed and correct."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

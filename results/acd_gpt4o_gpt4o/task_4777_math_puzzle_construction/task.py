class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "number_sequence", "constraints": "The sequence should follow a quadratic pattern with at least 5 terms. Provide the next term in the sequence."},
            "2": {"type": "logical_grid", "constraints": "Create a 3x3 magic square where the sum of each row, column, and diagonal is equal. Provide the sum as well."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle_type = t["type"]
        constraints = t["constraints"]
        instructions = f"""Your task is to construct a unique mathematical puzzle based on the given constraints and provide its solution.

Puzzle Type: {puzzle_type}
Constraints: {constraints}

In your response, include:
1. A clear statement of the puzzle.
2. The solution to the puzzle.
3. An explanation of how the puzzle meets the given constraints.

Your puzzle should be original, well-defined, and challenging. Provide your response in plain text format.

Response Format:
Puzzle: [Your puzzle statement here]
Solution: [Your solution here]
Explanation: [Your explanation here]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The puzzle should be clearly stated.",
            "The solution should be correct and clearly explained.",
            "The puzzle should meet the given constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

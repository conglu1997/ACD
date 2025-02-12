class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Construct a unique 3x3 magic square using the numbers 1 to 9 exactly once such that the sum of each row, column, and diagonal is the same. Ensure the solution is logically derived."},
            "2": {"puzzle": "You have 8 balls of equal size. 7 of them weigh the same, but one is heavier. You have a balance scale and can use it only twice. How can you determine which ball is heavier? Provide a step-by-step solution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following recreational math puzzle:

{t["puzzle"]}

Provide a detailed solution and explanation. Ensure your reasoning is clear and logically sound. Submit your response as a plain text string in the following format:

Solution: [Your solution here]
Explanation: [Your detailed explanation here]

Example Response for a different puzzle:
Solution: [Example Solution]
Explanation: [Example Explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should solve the puzzle correctly.",
            "The reasoning should be clear and logically sound.",
            "The answer should correctly address the puzzle's question."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

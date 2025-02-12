class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You are in a room with three doors. Each door has a sign. One sign says 'The treasure is behind this door.' The second sign says 'The treasure is not behind this door.' The third sign says 'The treasure is not behind door 1.' Only one of these signs is true. Which door has the treasure?"},
            "2": {"puzzle": "There are four boxes in a row, and each box contains one of the numbers 1, 2, 3, and 4. The boxes are labeled A, B, C, and D. The following statements are true: 1. Box A contains a number smaller than the number in Box B. 2. Box C contains an odd number. 3. Box D contains a number larger than the number in Box A. Determine the number in each box."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        puzzle = t["puzzle"]
        return f"""Solve the following puzzle: {puzzle} Provide your answer and reasoning as a plain text string in the following format:

Answer: [Your answer]
Reasoning: [Your detailed reasoning explaining how you arrived at the answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The answer should be correct based on the given puzzle.",
            "The reasoning should be clear, logical, and detailed.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

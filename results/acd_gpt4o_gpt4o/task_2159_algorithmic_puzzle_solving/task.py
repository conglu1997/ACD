class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Given a list of integers, find the longest increasing subsequence (LIS)."},
            "2": {"puzzle": "Given a list of integers, find the maximum sum subarray (MSS)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given algorithmic puzzle by providing a step-by-step solution.

Puzzle: {t['puzzle']}

Your response should include:
1. A clear and concise explanation of the approach you used to solve the puzzle.
2. The step-by-step solution to the puzzle.
3. Any relevant code or pseudocode to illustrate your solution.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of the approach should be clear and accurate.",
            "The step-by-step solution should be correct and complete.",
            "Any provided code or pseudocode should be relevant and accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

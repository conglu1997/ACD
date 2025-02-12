class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have 12 identical-looking balls, one of which is either heavier or lighter than the rest. You have a balance scale, and you can use it only three times. How can you determine which ball is the odd one out and whether it is heavier or lighter? Provide a detailed explanation of your solution."},
            "2": {"puzzle": "A farmer is traveling with a wolf, a goat, and a cabbage. He comes to a riverbank and finds a boat that can only carry himself and one other item at a time. If left together, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer get all three items across the river safely? Provide a detailed explanation of your solution."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the given mathematical puzzle and provide a detailed explanation of your solution. Ensure that your explanation is clear, logical, and includes all necessary steps to reach the solution. Provide your response in plain text format.\n\nPuzzle: {t['puzzle']}\n\nResponse format:\n1. Solution: [Your solution]\n2. Explanation: [Detailed explanation of how you arrived at the solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be correct and complete.", "The explanation should be clear, logical, and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

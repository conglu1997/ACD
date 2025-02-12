class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "A farmer has a wolf, a goat, and a cabbage and needs to cross a river with them. The farmer can take only one item at a time. If left alone, the wolf will eat the goat, and the goat will eat the cabbage. How can the farmer cross the river with all items intact?",
                "task_type": "solving"
            },
            "2": {
                "puzzle": "You have 12 balls, one of which is either heavier or lighter than the others. You have a balance scale and can use it three times. How can you find the different ball and determine if it is heavier or lighter?",
                "task_type": "solving"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical puzzle and provide a detailed explanation of your solution: {t['puzzle']}. Ensure that your explanation is clear, logical, and covers all necessary steps to arrive at the solution. Do not include any hints or partial solutions. Submit your response in the following format:

Solution: [Your solution here]
Explanation: [Detailed explanation of your solution here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The solution should be correct and complete.", "The explanation should be clear, logical, and cover all necessary steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

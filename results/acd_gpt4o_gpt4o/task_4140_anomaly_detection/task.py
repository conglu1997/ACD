class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "sequence": [2, 4, 6, 8, 10, 12, 15],
                "pattern": "Even numbers"
            },
            "2": {
                "sequence": [1, 1, 2, 3, 5, 8, 11, 13],
                "pattern": "Fibonacci sequence"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to identify the incorrect element in the given sequence based on the specified pattern. "
            "You need to analyze the sequence and determine which element does not conform to the given pattern. "
            "Provide a logical explanation for your choice to demonstrate your understanding of the pattern.\n\n"
            "Your response should be structured as follows: \n\n"
            "1. Incorrect element: [Your answer here] \n"
            "2. Explanation: [Your logical explanation here]"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["sequence"] == [2, 4, 6, 8, 10, 12, 15]:
            criteria = [
                "The response should identify 15 as the incorrect element.",
                "The explanation should state that 15 is not an even number."
            ]
        elif t["sequence"] == [1, 1, 2, 3, 5, 8, 11, 13]:
            criteria = [
                "The response should identify 11 as the incorrect element.",
                "The explanation should state that 11 does not follow the Fibonacci sequence pattern."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

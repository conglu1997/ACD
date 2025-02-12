class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"argument": "If we ban all cars, there will be fewer accidents. Therefore, we should ban all cars."},
            "2": {"argument": "You should not listen to her argument on climate change because she is not a scientist."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify and correct the logical fallacy in the following argument: '{t["argument"]}'. Provide a brief explanation of the fallacy and then rewrite the argument to remove the fallacy while maintaining the original intent. Your response should include two parts:
1. Explanation of the fallacy.
2. Corrected argument.
Ensure your response is clear and concise. Submit your response in the following format:
Explanation: [Your explanation here]
Corrected Argument: [Your corrected argument here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the logical fallacy.",
            "The explanation should be clear and accurate.",
            "The corrected argument should maintain the original intent without the fallacy.",
            "The response should follow the specified format: Explanation followed by Corrected Argument."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

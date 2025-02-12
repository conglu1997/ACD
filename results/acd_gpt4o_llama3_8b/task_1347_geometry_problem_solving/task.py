class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Calculate the area of a triangle with base 12 cm and height 9 cm."
            },
            "2": {
                "problem": "Find the area and circumference of a circle with a radius of 7 cm."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometry problem and provide a detailed explanation of your solution:

Problem: {t['problem']}

Ensure that your solution includes all necessary steps and calculations. Provide a clear and concise explanation of how you arrived at the answer. Submit your solution as a plain text string in the following format:

Solution: [Your solution here]
Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should include all necessary steps and calculations.",
            "The explanation should be clear and concise.",
            "The final answer should be correct and match the problem statement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

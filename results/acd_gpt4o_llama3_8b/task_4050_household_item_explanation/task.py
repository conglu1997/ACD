class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"item": "Refrigerator"},
            "2": {"item": "Washing Machine"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain how a {t['item']} works. Your explanation should be clear, accurate, and suitable for a general audience. Ensure that you cover the main components and their functions, as well as the overall working principle. Submit your response as a plain text string in the following format:

Explanation: [Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and easy to understand.",
            "The explanation should be accurate and cover the main components and their functions.",
            "The explanation should describe the overall working principle of the item.",
            "The explanation should be suitable for a general audience."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

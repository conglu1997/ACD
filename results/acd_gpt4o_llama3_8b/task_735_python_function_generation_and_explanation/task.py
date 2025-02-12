class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Write a Python function named 'fibonacci' that takes an integer n and returns the nth Fibonacci number."},
            "2": {"requirements": "Write a Python function named 'is_prime' that takes an integer n and returns True if n is a prime number and False otherwise."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given requirements:

Requirements: {t['requirements']}

Generate a Python function that meets the specified requirements. Additionally, provide a detailed explanation of how the function works, including the logic and any key programming concepts used. Submit your response as a plain text string with the following sections:
1. Function: [Your Python function]
2. Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a correct and functional Python function.",
            "The response should include a detailed explanation of how the function works.",
            "The explanation should cover the logic and key programming concepts used.",
            "The function should meet the specified requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

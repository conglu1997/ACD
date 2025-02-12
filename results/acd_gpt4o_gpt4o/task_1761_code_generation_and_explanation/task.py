class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Write a Python function that takes a list of integers and returns a new list with only the prime numbers.", "explanation": "Explain how your function works and why it correctly identifies prime numbers."},
            "2": {"problem": "Write a Python function that takes a string and returns the string with the characters reversed.", "explanation": "Explain how your function reverses the string and discuss its time complexity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a piece of Python code based on the given problem description and then provide a detailed explanation of the code.

Problem: {t['problem']}

After writing the code, explain how it works and why it solves the problem correctly. Your explanation should be clear, detailed, and include any relevant technical concepts. Provide your response in plain text format with the following structure:

Code:
[Your code here]

Explanation:
[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The code should correctly solve the given problem.",
            "The explanation should be clear and detailed.",
            "The explanation should accurately describe how the code works."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

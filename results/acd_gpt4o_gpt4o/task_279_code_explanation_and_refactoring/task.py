class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)"},
            "2": {"code": "def fibonacci(n):\n    if n <= 0:\n        return []\n    elif n == 1:\n        return [0]\n    elif n == 2:\n        return [0, 1]\n    else:\n        fibs = [0, 1]\n        for i in range(2, n):\n            fibs.append(fibs[-1] + fibs[-2])\n        return fibs"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following piece of code and then refactor it to improve its readability and efficiency.

Code:
{t['code']}

Instructions:
1. Provide a detailed explanation of what the code does, including its purpose and how it works.
2. Refactor the code to improve its readability and efficiency. Ensure that the refactored code produces the same output as the original.
3. Provide the refactored code and explain the changes you made to improve it.

Your response should be in the following format:
Explanation: [Your explanation]
Refactored Code: [Your refactored code]
Changes: [Explanation of changes]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should clearly describe the purpose and functionality of the original code.", "The refactored code should be more readable and efficient while producing the same output.", "The explanation of changes should justify the improvements made."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

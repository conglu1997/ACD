class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "buggy_code": "def calculate_sum(n):\n    total = 0\n    for i in range(1, n+1):\n        total += i\n    return total\n# The function should return the sum of the first n natural numbers, but it has a bug.",
                "expected_output": "calculate_sum(5) should return 15"
            },
            "2": {
                "buggy_code": "def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num**0.5) + 1):\n        if num % i == 0,\n            return False\n    return True\n# The function should return True if the number is prime and False otherwise, but it has a bug.",
                "expected_output": "is_prime(4) should return False"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        buggy_code = t['buggy_code']
        expected_output = t['expected_output']
        return f"""Identify and fix the bugs in the following code to ensure it performs the intended function correctly. The expected output for a test case is provided for reference.
\n{buggy_code}\n\nExpected Output: {expected_output}\n\nSubmit your fixed code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submitted code should fix the identified bugs.",
            "The fixed code should produce the correct output for the provided test case.",
            "The fixed code should maintain the original function's purpose."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

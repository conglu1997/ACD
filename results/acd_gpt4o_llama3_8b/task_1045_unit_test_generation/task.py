class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "function": "def add(a, b):\n    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):\n        raise ValueError(\"Inputs must be numbers\")\n    return a + b"
            },
            "2": {
                "function": "def is_prime(n):\n    if not isinstance(n, int) or n <= 0:\n        raise ValueError(\"Input must be a positive integer\")\n    if n == 1:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Given the following Python function, generate a set of unit tests to verify its correctness. The unit tests should cover a range of edge cases and typical cases. Submit your response as a Python code string defining the unit tests, using the unittest framework.

Function:
{t['function']}

Ensure your unit tests are comprehensive and correctly verify the function's behavior. The unit tests should be written using the unittest framework and include both positive and negative test cases. Submit your response as a Python code string. Here is an example format for a unit test:

import unittest

class TestFunction(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The unit tests should cover a range of edge cases and typical cases.",
            "The unit tests should be written using the unittest framework.",
            "The unit tests should verify the correctness of the function's behavior.",
            "The unit tests should include both positive and negative test cases."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

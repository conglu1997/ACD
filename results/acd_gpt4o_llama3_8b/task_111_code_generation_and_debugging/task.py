class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Write a Python function that calculates the factorial of a number.",
                "debug": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5)) # Should print 120"
            },
            "2": {
                "prompt": "Write a Python function that checks if a given string is a palindrome.",
                "debug": "def is_palindrome(s):\n    s = s.replace(' ', '').lower()\n    return s == s[::-1]\n\nprint(is_palindrome('A man a plan a canal Panama')) # Should print True"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given two tasks. First, generate a piece of Python code based on the given prompt. Second, find and correct the bug in the provided faulty code.

Task 1: {t['prompt']}
Task 2: Debug the following code:
{t['debug']}

Submit your response in the following format:
Code: [Your generated code]
Debugged Code: [Your corrected code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated code should correctly fulfill the prompt requirements.",
            "The debugged code should be free of syntax and logical errors.",
            "The response should include both tasks in the correct format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def find_max(nums):\n    max_num = float('-inf')\n    for i in range(len(nums)):\n        if nums[i] > max_num:\n            max_num = nums[i]\n    return max_num", "description": "Debug this code snippet to correctly find the maximum value in a list of numbers."},
            "2": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n\nresult = factorial(5)\nprint(result)", "description": "Optimize this code snippet to compute the factorial of a number more efficiently."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a code snippet and a description of the task. Your goal is to debug or optimize the code as per the given description. Submit the corrected or optimized code as a plain text string.

Code Snippet:
{t['code']}

Description:
{t['description']}

Your submission should be a single plain text string with the corrected or optimized code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

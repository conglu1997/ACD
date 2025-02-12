class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code_snippet": "def find_max(nums):\n    if not nums:\n        return None\n    max_num = nums[0]\n    for num in nums[1:]:\n        if num > max_num:\n            max_num = num\n    return max_num\n\n# Example usage:\n# print(find_max([1, 2, 3, 4]))"},
            "2": {"code_snippet": "import re\n\ndef is_palindrome(s):\n    s = s.lower()\n    s = re.sub(r'[^a-z0-9]', '', s)\n    return s == s[::-1]\n\n# Example usage:\n# print(is_palindrome('A man, a plan, a canal, Panama'))"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and fix the errors in the following code snippet. Ensure that the corrected code runs as intended and produces the correct output. Do not introduce any new functionality beyond what is necessary to fix the errors. Here is the code snippet:\n\n{t['code_snippet']}\n\nSubmit your corrected code in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The corrected code should run without errors.", "The corrected code should produce the correct output for the given example usage.", "The corrected code should not introduce any new functionality beyond what is necessary to fix the errors."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

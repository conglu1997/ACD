class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def merge_sort(arr):\n    if len(arr) > 1: \n        mid = len(arr) // 2\n        L = arr[:mid]\n        R = arr[mid:]\n        merge_sort(L)\n        merge_sort(R)\n        i = j = k = 0\n        while i < len(L) and j < len(R):\n            if L[i] < R[j]:\n                arr[k] = L[i]\n                i += 1\n            else:\n                arr[k] = R[j]\n                j += 1\n            k += 1\n        while i < len(L):\n            arr[k] = L[i]\n            i += 1\n            k += 1\n        while j < len(R):\n            arr[k] = R[j]\n            j += 1\n            k += 1"},
            "2": {"comments": "# This function checks if a number is prime\n# It takes an integer as input\n# It returns False if the number is less than 2\n# It checks for factors from 2 to the square root of the number\n# If a factor is found, it returns False\n# If no factors are found, it returns True"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'code' in t:
            instructions = f"""Your task is to generate comments that describe the functionality of the following code:

Code:
{t['code']}

Ensure that your comments are clear, accurate, and provide a step-by-step explanation of what the code does. Provide your comments in plain text format, with each comment on a new line corresponding to the code it describes. Your response should be structured as follows:

Comments:
[Your comments]"""
        else:
            instructions = f"""Your task is to generate a piece of code based on the following comments:

Comments:
{t['comments']}

Ensure that your code accurately reflects the functionality described in the comments. Provide your code in plain text format. Your response should be structured as follows:

Code:
[Your code]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'code' in t:
            criteria = ["The comments should accurately describe the functionality of the code."]
        else:
            criteria = ["The code should accurately reflect the functionality described in the comments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

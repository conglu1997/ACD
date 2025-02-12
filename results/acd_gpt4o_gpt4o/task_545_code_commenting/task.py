class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "generate_comment", "code": "def merge_sort(arr):\n    if len(arr) > 1:\n        mid = len(arr) // 2\n        left_half = arr[:mid]\n        right_half = arr[mid:]\n        merge_sort(left_half)\n        merge_sort(right_half)\n        i = j = k = 0\n        while i < len(left_half) and j < len(right_half):\n            if left_half[i] < right_half[j]:\n                arr[k] = left_half[i]\n                i += 1\n            else:\n                arr[k] = right_half[j]\n                j += 1\n            k += 1\n        while i < len(left_half):\n            arr[k] = left_half[i]\n            i += 1\n            k += 1\n        while j < len(right_half):\n            arr[k] = right_half[j]\n            j += 1\n            k += 1"},
            "2": {"type": "interpret_comment", "code": "# This function checks if a number is prime\ndef is_prime(n):\n    # Edge cases\n    if n <= 1:\n        return False\n    if n <= 3:\n        return True\n    # Check for divisibility\n    if n % 2 == 0 or n % 3 == 0:\n        return False\n    i = 5\n    while i * i <= n:\n        if n % i == 0 or n % (i + 2) == 0:\n            return False\n        i += 6\n    return True"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "generate_comment":
            code = t["code"]
            instructions = f"""Your task is to generate meaningful comments for the given code snippet.

Code snippet:
{code}

Ensure that the comments accurately describe the functionality of each part of the code. Provide your comments in plain text format, with each comment placed appropriately in the code."""
        elif t["type"] == "interpret_comment":
            code = t["code"]
            instructions = f"""Your task is to interpret the functionality of the given code snippet based on the existing comments.

Code snippet:
{code}

Provide a clear and concise description of what the code does, ensuring that your interpretation is accurate and comprehensive. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "generate_comment":
            criteria = [
                "The comments should accurately describe the functionality of each part of the code.",
                "The comments should be clear, concise, and placed appropriately in the code."
            ]
        elif t["type"] == "interpret_comment":
            criteria = [
                "The interpretation should be accurate and comprehensive.",
                "The description should be clear and concise."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

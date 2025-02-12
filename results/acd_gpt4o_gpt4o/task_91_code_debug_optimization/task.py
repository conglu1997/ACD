class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def sum_of_squares(n):\n    total = 0\n    for i in range(1, n+1):\n        total += i * i\n    return total\n\n# Bug: Should return 0 for n <= 0 but currently does not handle it.", "description": "Fix the bug in the function so that it returns 0 for n <= 0."},
            "2": {"code": "def find_max(arr):\n    max_val = arr[0]\n    for val in arr:\n        if val > max_val:\n            max_val = val\n    return max_val\n\n# Optimization: The function works correctly but can be optimized for readability and performance.", "description": "Optimize the function for better readability and performance."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        code = t["code"]
        description = t["description"]
        instructions = f"""Your task is to analyze the following code snippet and perform the specified action:\n\nCode:\n{code}\n\nDescription:\n{description}\n\nPlease provide the corrected or optimized code in plain text format. Ensure that your solution maintains the original functionality and adheres to the specified requirements. Your response should be formatted as follows:\n\nCorrected/Optimized Code:\n[Your code here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should correctly handle the specified bug or optimization.",
            "The submission should maintain the original functionality of the code.",
            "The submission should be syntactically correct and executable."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

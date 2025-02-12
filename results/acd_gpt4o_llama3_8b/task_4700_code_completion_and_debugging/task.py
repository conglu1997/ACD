class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "partial_code": "def find_max(numbers):\n    # Initialize the maximum number\n    max_num = numbers[0]\n    # Iterate through the list\n    for num in numbers: \n        if num > max_num: \n            max_num = num\n    # Return the maximum number\n    return max_num",
                "test_case": [3, 1, 4, 1, 5, 9, 2, 6, 5],
                "expected_output": 9
            },
            "2": {
                "buggy_code": "def calculate_average(numbers):\n    total = 0\n    count = len(numbers)\n    for num in numbers:\n        total += num\n    average = total / count\n    return average\n\n# Example usage\nnumbers = [1, 2, 3, 4, 5]\nprint(calculate_average(numbers))",
                "expected_output": 3.0
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'partial_code' in t:
            return f"""Complete the following partially written Python code. Ensure that the completed function works correctly and efficiently. Test your implementation using the provided test case to verify that it produces the expected output. Submit the completed code as a plain text string in the following format:\n\nCompleted Code:\n[Your completed code here]"""
        elif 'buggy_code' in t:
            return f"""Debug the following Python code snippet to make it functional. Ensure that the corrected code works as intended and produces the expected output. Test your corrected code to verify it produces the expected output. Submit the corrected code as a plain text string in the following format:\n\nCorrected Code:\n[Your corrected code here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "For Task 1: The completed code should correctly find the maximum number in the list and be syntactically correct. It should produce the expected output when tested with the provided test case.",
            "For Task 2: The corrected code should accurately calculate the average of the numbers in the list and be free of syntax errors. It should produce the expected output when tested with the given example."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

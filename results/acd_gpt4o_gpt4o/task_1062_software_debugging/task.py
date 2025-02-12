class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def calculate_area(radius):\n    pi = 3.14\n    area = pi * radius ** 2\n    return area\n\n# Example usage\nprint(calculate_area(5))", "bug": "The function should raise an error for negative radius."},
            "2": {"code": "def find_max(numbers):\n    max_num = numbers[0]\n    for num in numbers:\n        if num > max_num:\n            max_num = num\n    return max_num\n\n# Example usage\nprint(find_max([1, 2, 3, 4, 5]))", "bug": "The function should handle empty lists by returning None."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and correct errors in the following piece of code:

Code:
{t["code"]}

The specific bug to address is:
{t["bug"]}

Provide your corrected code in plain text format. Ensure your corrected code runs correctly without any errors.

Example format for your response:

Corrected Code:
def calculate_area(radius):
    if radius < 0:
        raise ValueError('Radius cannot be negative')
    pi = 3.14
    area = pi * radius ** 2
    return area

print(calculate_area(5))"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The corrected code should address the specified bug.",
            "The corrected code should not introduce new errors.",
            "The corrected code should be syntactically correct and executable."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

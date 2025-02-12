class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def calculate_area(radius):\n    area = 3.14 * radius ** 2\n    return area\n\nprint(calculate_area(5))"},
            "2": {"code": "def greet(name):\n    print(f'Hello, {name}!')\n\ngreet('Alice')\ngreet('Bob')"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to identify and fix any errors in the given code snippet and then refactor the code to improve its readability and efficiency. Ensure the code runs correctly and adheres to best practices. Provide your response in plain text format including the corrected and refactored code.

Code Snippet:
{t['code']}

Your response should include:
1. Fixed Code: [Your fixed code]
2. Refactored Code: [Your refactored code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The fixed code should correctly identify and fix any errors in the original snippet.",
            "The refactored code should improve readability and efficiency without changing the original functionality.",
            "The response should include both the fixed code and the refactored code.",
            "The fixed and refactored code should run correctly and produce the expected output."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

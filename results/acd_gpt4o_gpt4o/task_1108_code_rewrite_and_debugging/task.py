class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def greet(name):\n    return f'Hello, {name}!'\n", "constraints": "Rewrite the function to return a greeting in uppercase letters. Ensure that the function still returns a string and handles non-string inputs gracefully."},
            "2": {"code": "def add(a, b):\n    return a - b\n", "constraints": "Debug the function to return the correct sum of two numbers. Ensure that the function handles both positive and negative integers, as well as zero, correctly."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to rewrite or debug the given piece of code to satisfy the new constraints or fix errors while meeting functional requirements.

Original Code:
{t["code"]}

Constraints:
{t["constraints"]}

Ensure that the revised code meets the constraints and functions correctly. Provide your revised code in plain text format, clearly presented as a complete function."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The revised code should satisfy the given constraints.",
            "The revised code should function correctly and produce the expected output.",
            "The code should be syntactically correct and free of errors.",
            "The function should handle edge cases appropriately.",
            "The function should handle non-string inputs (Task 1) or zero (Task 2) appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

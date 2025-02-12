class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "function": "def add(a, b):\n    return a + b",
                "description": "A simple function that takes two arguments and returns their sum."
            },
            "2": {
                "function": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
                "description": "A recursive function that computes the factorial of a given non-negative integer."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        function_code = t["function"]
        instructions = f"""Your task is to generate comprehensive technical documentation for the following function.

Function Code:
{function_code}

Ensure your documentation includes:
1. A brief description of the function.
2. A detailed explanation of the function's parameters and return value.
3. Any potential edge cases or important notes.
4. An example usage of the function.

Provide your documentation in plain text format. Structure it as follows:

Description: [Brief description]
Parameters: [Detailed explanation of parameters]
Return Value: [Detailed explanation of return value]
Notes: [Any potential edge cases or important notes]
Example: [Example usage of the function]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The documentation should include a brief description of the function.",
            "The documentation should explain the function's parameters and return value.",
            "The documentation should mention any potential edge cases or important notes.",
            "The documentation should provide an example usage of the function.",
            "The documentation should correctly explain the logic of the function."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

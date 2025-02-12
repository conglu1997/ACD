class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "functions": [
                    "def add(a: int, b: int) -> int: \"\"\"Adds two integers together.\"\"\"\n    return a + b",
                    "def multiply(a: int, b: int) -> int: \"\"\"Multiplies two integers together.\"\"\"\n    return a * b"
                ]
            },
            "2": {
                "functions": [
                    "def factorial(n: int) -> int: \"\"\"Calculates the factorial of a non-negative integer.\"\"\"\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)",
                    "def fibonacci(n: int) -> int: \"\"\"Calculates the nth Fibonacci number.\"\"\"\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n - 1) + fibonacci(n - 2)",
                    "def is_prime(n: int) -> bool: \"\"\"Checks if a number is a prime number.\"\"\"\n    if n <= 1:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task:

Generate API documentation for the provided functions. The documentation should include:
1. A brief description of what each function does.
2. An explanation of each parameter, including its type and purpose.
3. The return type and a brief description of the return value.
4. An example of usage for each function.

Functions:
{', '.join(t['functions'])}

Ensure that your documentation is clear, concise, and correctly formatted. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The documentation should include a brief description of each function.",
            "The documentation should explain each parameter, including its type and purpose.",
            "The documentation should describe the return type and value.",
            "The documentation should include an example of usage for each function."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

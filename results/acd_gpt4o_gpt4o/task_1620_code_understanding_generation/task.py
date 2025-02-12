class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)",
                "problem": "Write a function that calculates the factorial of a number using iteration instead of recursion.",
                "expected_output": "def iterative_factorial(n):\n    result = 1\n    while n > 0:\n        result *= n\n        n -= 1\n    return result"
            },
            "2": {
                "code": "def is_prime(num):\n    if num <= 1:\n        return False\n    for i in range(2, int(num**0.5) + 1):\n        if num % i == 0:\n            return False\n    return True",
                "problem": "Write a function that returns the first N prime numbers.",
                "expected_output": "def first_n_primes(N):\n    primes = []\n    num = 2\n    while len(primes) < N:\n        if is_prime(num):\n            primes.append(num)\n        num += 1\n    return primes"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to understand the given piece of code and generate a new piece of code to solve the specified problem.

Given Code: {t['code']}
Problem: {t['problem']}

Provide your solution in plain text format as a complete function definition."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated code should correctly solve the specified problem.",
            "The code should be syntactically correct and executable.",
            "The solution should be provided as a complete function definition."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

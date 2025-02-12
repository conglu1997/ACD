class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "Python", "target_language": "JavaScript", "code": "def fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n-1) + fibonacci(n-2)\n\ndef sum_of_fibonacci(n):\n    total = 0\n    for i in range(n):\n        total += fibonacci(i)\n    return total", "expected_result": "function fibonacci(n) {\n    if (n <= 0) {\n        return 0;\n    } else if (n === 1) {\n        return 1;\n    } else {\n        return fibonacci(n-1) + fibonacci(n-2);\n    }\n}\n\nfunction sumOfFibonacci(n) {\n    let total = 0;\n    for (let i = 0; i < n; i++) {\n        total += fibonacci(i);\n    }\n    return total;\n}"},
            "2": {"source_language": "JavaScript", "target_language": "Python", "code": "function factorial(n) {\n    if (n === 0) {\n        return 1;\n    } else {\n        return n * factorial(n - 1);\n    }\n}\n\nfunction sumOfFactorials(n) {\n    let total = 0;\n    for (let i = 1; i <= n; i++) {\n        total += factorial(i);\n    }\n    return total;\n}", "expected_result": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\ndef sum_of_factorials(n):\n    total = 0\n    for i in range(1, n + 1):\n        total += factorial(i)\n    return total"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following code from {t['source_language']} to {t['target_language']}. Ensure that the translated code preserves the original functionality and is syntactically correct.\n\nSource Code:\n{t['code']}\n\nProvide your translation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The translated code should preserve the original functionality and match the expected result: {t['expected_result']}."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

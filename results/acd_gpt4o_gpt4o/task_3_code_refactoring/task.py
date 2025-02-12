class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def inefficient_sum(n):\n    result = 0\n    for i in range(1, n+1):\n        for j in range(1, i+1):\n            result += 1\n    return result", "expected_output": "(n * (n + 1)) // 2"},
            "2": {"code": "def inefficient_fibonacci(n):\n    if n <= 1:\n        return n\n    return inefficient_fibonacci(n-1) + inefficient_fibonacci(n-2)", "expected_output": "def efficient_fibonacci(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to refactor the given code to improve its efficiency. Here's the code you need to refactor:\n{t['code']}\nPlease provide the refactored code as your submission in the same format as the original."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The refactored code should be more efficient than the original.", "The refactored code should produce the same output as the original."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

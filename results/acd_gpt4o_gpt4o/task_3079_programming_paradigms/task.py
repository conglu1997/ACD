class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"paradigm1": "imperative", "paradigm2": "functional", "code": "def factorial(n):\n    result = 1\n    for i in range(1, n + 1):\n        result *= i\n    return result"},
            "2": {"paradigm1": "object-oriented", "paradigm2": "functional", "code": "class Counter:\n    def __init__(self):\n        self.count = 0\n    def increment(self):\n        self.count += 1\n    def get_count(self):\n        return self.count"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to convert the given code from the {t['paradigm1']} paradigm to the {t['paradigm2']} paradigm. Additionally, provide a detailed explanation of the differences between the two paradigms and how those differences are reflected in your code conversion. Here is the code:\n\n{t['code']}\n\nSubmit your solution in plain text format. Your response should include:\n1. The converted code.\n2. An explanation of the differences between the two paradigms.\n3. A discussion of how these differences are reflected in your code conversion."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The converted code should be accurate and follow the target paradigm.", "The explanation should clearly highlight the differences between the paradigms.", "The discussion should relate the differences to the code conversion.", "The response should be well-structured and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

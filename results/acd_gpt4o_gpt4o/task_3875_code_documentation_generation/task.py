class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def add_numbers(a, b):\n    '''\n    Adds two numbers together.\n    '''\n    return a + b"},
            "2": {"code": "def fibonacci(n):\n    '''\n    Generates the nth Fibonacci number.\n    '''\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given Python code and generate comprehensive documentation. The documentation should include:\n1. A clear and concise description of the function's purpose.\n2. Explanations for each parameter.\n3. A usage example demonstrating how to call the function.\n\nHere is the code:\n{t['code']}\n\nProvide your documentation in the following format:\n\nFunction Description: [Your description]\nParameters: [Your parameter explanations]\nUsage Example: [Your usage example]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The documentation should accurately describe the function's purpose.",
            "The parameter explanations should be clear and correct.",
            "The usage example should correctly demonstrate how to call the function."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Calculate the factorial of a number.", "example": "factorial(5)"},
            "2": {"problem": "Generate the nth Fibonacci number.", "example": "fibonacci(7)"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a recursive function in Python to solve the following problem and provide a detailed explanation of how the function works step-by-step:

Problem: {t['problem']}

Example: {t['example']}

Please submit the function and the explanation separately in plain text."
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function should be implemented correctly and should be recursive.",
            "The explanation should clearly describe the recursive process step-by-step.",
            "The function should solve the problem as described in the instructions.",
            "The response should be in plain text format.",
            "The function and explanation should be submitted separately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def factorial(n):\n    if n == 0:  # base case for recursion\n        return 1\n    else:  # recursive case\n        return n * factorial(n-1)"},
            "2": {"code": "def fibonacci(n):\n    a, b = 0, 1  # initialize first two numbers\n    for _ in range(n):  # iterate n times\n        a, b = b, a + b  # update a and b\n    return a  # return the nth Fibonacci number"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to add meaningful comments to the following code snippet to explain what it does. Ensure that the comments are clear and helpful. Here is the code snippet:\n\n{t['code']}\n\nSubmit your comments as in-line comments within the code, using the '#' symbol."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The comments should accurately describe the functionality of the code.", "The comments should be clear and written in proper English.", "All parts of the code should be covered."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

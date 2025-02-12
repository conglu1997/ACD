class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem_statement": "Write a function that takes a list of integers and returns a list of those integers sorted in ascending order. Your function should handle an empty list and a list with one element."},
            "2": {"problem_statement": "Write a function that takes a positive integer n and returns the nth Fibonacci number. Your function should handle the first few Fibonacci numbers correctly (e.g., F(0) = 0, F(1) = 1)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Implement the following algorithm in Python: {t['problem_statement']} Submit your solution as a plain text string containing the Python code. Ensure your code is syntactically correct and handles edge cases described in the problem statement."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should be valid Python code.",
            "The code should correctly implement the described algorithm.",
            "The code should be logically sound and produce the correct output for valid inputs, including edge cases.",
            "The code should follow standard programming practices.",
            "The code should be efficient and avoid unnecessary computations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

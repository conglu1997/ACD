class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code_snippet": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)", "task_type": "explain"},
            "2": {"requirements": "Write a Python function that takes a list of integers and returns a new list where all even numbers are doubled and all odd numbers are tripled.", "task_type": "generate"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'explain':
            return f"Explain the functionality of the following code snippet:\n\n{t['code_snippet']}\n\nSubmit your explanation as a plain text string."
        elif t['task_type'] == 'generate':
            return f"{t['requirements']}\n\nSubmit your code as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'explain':
            criteria = ["The explanation should correctly describe the functionality of the code snippet."]
        elif t['task_type'] == 'generate':
            criteria = ["The code should correctly implement the specified functionality."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

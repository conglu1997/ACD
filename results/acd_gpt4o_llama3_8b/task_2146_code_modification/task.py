class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"code": "def add(a, b):\n    return a - b\n\nresult = add(5, 3)\nprint(result)", "objective": "Modify the code so that it correctly adds two numbers."},
            "2": {"code": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nresult = factorial(5)\nprint(result)", "objective": "Modify the code to use a loop instead of recursion to calculate the factorial of a number."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        code = t['code']
        objective = t['objective']
        return f"""You are given a piece of code and an objective. Your task is to modify the code to achieve the specified objective. Ensure that the modified code is syntactically correct and achieves the desired functionality.

Code:
{code}

Objective: {objective}

Submit your modified code as a plain text string in the following format:

Modified Code: [Your modified code]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The modified code should be syntactically correct.",
            "The modified code should achieve the specified objective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

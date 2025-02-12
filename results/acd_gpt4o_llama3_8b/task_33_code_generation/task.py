class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"function_name": "square", "description": "Create a function called square that takes an integer and returns its square."},
            "2": {"function_name": "is_even", "description": "Create a function called is_even that takes an integer and returns True if it is even and False if it is odd."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        function_name = t["function_name"]
        description = t["description"]
        return f"""Generate a Python function based on the following description:

Function Name: {function_name}
Description: {description}

Ensure the function is complete, correct, and follows Python syntax. The function should have proper indentation and be executable. Submit your function as a plain text string in the following format:

def {function_name}(param):
    # your code here
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function should be syntactically correct.",
            "The function should have the correct return type.",
            "The function should correctly implement the described behavior."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

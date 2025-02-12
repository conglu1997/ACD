class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "specification": "Implement a function that takes a list of integers and returns a new list with each integer squared. If the input list is empty, return an empty list.",
                "code": "def square_integers(int_list):\n    if not int_list:\n        return None\n    return [x**2 for x in int_list]"
            },
            "2": {
                "specification": "Implement a function that takes a string and returns the string reversed. If the input string is empty, return an empty string.",
                "code": "def reverse_string(s):\n    if len(s) == 0:\n        return s[::-1]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following two parts:

1. Create a function based on the given specification.
2. Debug the provided piece of code if there are any errors.

Specification: {t['specification']}

Code: {t['code']}

Provide your solutions in plain text format. For the first part, include the function definition and implementation. For the second part, include the corrected code if there are any errors, or state that the code is correct.

Here is an example of how to format your response:

Function Implementation:
def example_function():
    # function code

Debugged Code:
def example_function():
    # corrected code (if applicable)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The function implementation should meet the given specification.",
            "The debugged code should be syntactically correct and functional."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

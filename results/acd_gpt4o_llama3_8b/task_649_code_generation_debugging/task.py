class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_description": "Write a Python function that takes a list of integers and returns a new list containing only the even numbers, sorted in ascending order.",
                "requirements": ["Function name: filter_and_sort_evens", "Input: list of integers", "Output: list of integers"]
            },
            "2": {
                "problem_description": "Debug the following Python code snippet which is supposed to calculate the factorial of a given number:",
                "code_snippet": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(factorial(5))",
                "expected_output": "120"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'requirements' in t:
            return f"""Write a Python function based on the following problem description and requirements. Ensure that your function meets all the requirements.

Problem Description:
{t['problem_description']}

Requirements:
{', '.join(t['requirements'])}

Submit your function as a plain text string."""
        else:
            return f"""Debug the following Python code snippet to meet the expected output. Identify and fix any errors in the code.

Code Snippet:
{t['code_snippet']}

Expected Output:
{t['expected_output']}

Submit your corrected code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'requirements' in t:
            criteria = [
                "The function should be named 'filter_and_sort_evens'.",
                "The function should take a list of integers as input.",
                "The function should return a list of integers.",
                "The function should correctly filter out the even numbers and sort them in ascending order."
            ]
        else:
            criteria = [
                "The submitted code should correctly calculate the factorial of the given number.",
                "The submission should meet the expected output of 120 for the input of 5.",
                "The code should not contain syntax errors or logical bugs."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
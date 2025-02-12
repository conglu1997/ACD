class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write a function that takes a list of integers and returns a new list with only the even numbers, sorted in ascending order.",
                "constraints": "The function should be named filter_and_sort_evens. The input list will contain at most 1000 integers, each between -1000 and 1000.",
                "example_input": "[5, 3, 8, 6, 7, 2]",
                "example_output": "[2, 6, 8]"
            },
            "2": {
                "problem": "Write a function that takes a string and returns the string reversed, preserving the case of each character.",
                "constraints": "The function should be named reverse_string_preserve_case. The input string will contain at most 1000 characters.",
                "example_input": "HelloWorld",
                "example_output": "dlroWolleH"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Python function to solve the following problem:

Problem: {t['problem']}
Constraints: {t['constraints']}

Example Input: {t['example_input']}
Example Output: {t['example_output']}

Ensure your function adheres to the constraints and solves the problem correctly. The function should handle edge cases appropriately. Submit your function as a plain text string. Your submission should only include the function definition and nothing else."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The function name should match exactly as given in the constraints.",
            "The function should solve the problem correctly.",
            "The function should handle edge cases appropriately.",
            "The function should produce the correct output for the example input provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

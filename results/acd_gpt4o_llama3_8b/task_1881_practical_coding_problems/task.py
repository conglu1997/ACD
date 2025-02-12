class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Write a Python function that takes a list of integers and returns the sum of all even numbers in the list."
            },
            "2": {
                "problem": "Write a Python function that takes a string as input and returns the string reversed, but with the order of words maintained. For example, 'Hello World' should become 'olleH dlroW'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Python function to solve the following problem:

Problem: {t['problem']}

Ensure your function is correct, efficient, and adheres to standard coding practices. Provide the complete function definition and any necessary imports. Your response should include:
1. The complete function definition.
2. Any necessary import statements.
3. Example usage of the function.

Submit your response as a plain text string in the following format:

Function Definition:
[Your function definition]

Example Usage:
[Your example usage]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The function should correctly solve the problem.",
            "The function should be efficient and adhere to standard coding practices.",
            "The submission should include the complete function definition and any necessary imports.",
            "The submission should include example usage of the function."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

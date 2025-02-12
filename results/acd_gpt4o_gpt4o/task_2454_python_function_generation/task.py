class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create a function that takes a list of integers and returns the sum of the even numbers.", "example_input": [1, 2, 3, 4], "example_output": 6},
            "2": {"description": "Create a function that takes a string and returns a dictionary with the count of each character.", "example_input": "hello", "example_output": {"h": 1, "e": 1, "l": 2, "o": 1}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to translate the following natural language description into a Python function. Ensure that your function is syntactically correct and performs the specified task accurately.

Description: {t['description']}

Your function should be defined as follows:

    def your_function_name(parameters):
        # Your code here
        return result

Test your function with the following example input/output to verify its correctness:

Example Input: {t['example_input']}
Example Output: {t['example_output']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The function should be syntactically correct.", "The function should perform the specified task accurately.", "The function should return the correct output for the given example input."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

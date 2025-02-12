class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write a Python function named `sort_descending` that takes a list of numbers and returns the list sorted in descending order. Do not use built-in sorting functions.", "example_input": [5, 3, 8, 1, 2], "example_output": [8, 5, 3, 2, 1]},
            "2": {"description": "Write a Python function named `char_count` that takes a string and returns a dictionary where the keys are characters and the values are the counts of each character in the string.", "example_input": "hello", "example_output": {"h": 1, "e": 1, "l": 2, "o": 1}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a Python function based on the following description:

{t['description']}

Example Input: {t['example_input']}
Example Output: {t['example_output']}

Submit your response as a plain text string containing the Python code."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'sort_descending' in t['description']:
            criteria = ["The code must correctly implement a sorting algorithm.", "The code must not use built-in sorting functions.", "The function must return the list sorted in descending order.", "The function name must be 'sort_descending'."]
        elif 'char_count' in t['description']:
            criteria = ["The code must correctly create a dictionary of character counts.", "The function must iterate over the string to count characters.", "The function name must be 'char_count'."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
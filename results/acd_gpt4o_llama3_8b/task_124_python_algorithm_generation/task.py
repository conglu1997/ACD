class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem_description": "Write a Python function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string.", "example": "Input: ['flower', 'flow', 'flight'] Output: 'fl'", "synthetic_examples": ["Input: ['dog', 'racecar', 'car'] Output: ''", "Input: ['interspecies', 'interstellar', 'interstate'] Output: 'inters'"]},
            "2": {"problem_description": "Write a Python function that takes a list of integers and returns the longest increasing subsequence.", "example": "Input: [10, 9, 2, 5, 3, 7, 101, 18] Output: [2, 3, 7, 101]", "synthetic_examples": ["Input: [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] Output: [0, 2, 6, 9, 11, 15]", "Input: [3, 10, 2, 1, 20] Output: [3, 10, 20]"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        examples = '\n'.join(t.get('synthetic_examples', []))
        return f"""Generate Python code to solve the following problem: {t['problem_description']} Provide a complete function definition without any additional explanation. Example input and output: {t['example']}\nAdditional examples:\n{examples}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

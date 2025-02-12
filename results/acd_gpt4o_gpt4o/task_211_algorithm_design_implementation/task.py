class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design and implement an algorithm to find the longest common subsequence between two strings.", "example_input": ["ABCBDAB", "BDCAB"], "example_output": "BCAB"},
            "2": {"problem": "Design and implement an algorithm to sort an array of integers using the merge sort technique.", "example_input": [38, 27, 43, 3, 9, 82, 10], "example_output": [3, 9, 10, 27, 38, 43, 82]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design and implement an algorithm to solve the following problem:

{t["problem"]}

Example input: {t["example_input"]}
Expected output: {t["example_output"]}

Provide your solution in Python code. Ensure your code is correct, efficient, and well-documented with comments explaining the key steps."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The code should correctly solve the given problem.",
            "The code should be efficient and follow best practices.",
            "The code should be well-documented with comments explaining the key steps.",
            "The code should produce the expected output for the given example input."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

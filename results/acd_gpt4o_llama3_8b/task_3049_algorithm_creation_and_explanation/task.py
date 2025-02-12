class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem_description": "Given an array of integers, find the contiguous subarray with the largest sum and return that sum. Provide the solution in Python code and include an explanation with time and space complexity."},
            "2": {"problem_description": "Given a string, find the length of the longest substring without repeating characters. Provide the solution in Python code and include an explanation with time and space complexity."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks:

1. Create an algorithm to solve the given problem: '{t["problem_description"]}'. Provide the algorithm in Python code.

2. Explain the algorithm you created. Your explanation should include the logic behind the algorithm, why it works, and its time and space complexity. Submit your response in the following format:

Algorithm: [Your algorithm in Python code]
Explanation: [Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should be correct and solve the problem as described.",
            "The explanation should clearly describe the logic behind the algorithm, why it works, and its time and space complexity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

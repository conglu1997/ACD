class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Given a list of integers, return the indices of the two numbers that add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice. Example: Input: nums = [2, 7, 11, 15], target = 9. Output: [0, 1]."},
            "2": {"problem": "Given a string s, find the length of the longest substring without repeating characters. Example: Input: s = 'abcabcbb'. Output: 3."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        return f"""Solve the following algorithmic problem by writing a Python function. The function should be named 'solve'. Submit your solution as a plain text string containing your code.

Problem: {problem}

Your solution should be in the following format:

def solve(nums, target):
    # Your code here
    return [index1, index2]

The function should take the specified inputs and return the correct outputs as described in the problem statement. Ensure that your code is efficient and handles edge cases appropriately."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should be a valid Python function.", "The function should correctly solve the problem as described.", "The solution should be efficient and handle edge cases appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

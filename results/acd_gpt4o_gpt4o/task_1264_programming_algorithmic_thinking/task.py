class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice. Example: Given nums = [2, 7, 11, 15], target = 9, because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1]."},
            "2": {"problem": "Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string ''. Example: Given strs = ['flower', 'flow', 'flight'], the longest common prefix is 'fl'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to solve the following programming problem and provide a detailed explanation of your solution:

Problem: {problem}

Your response should include:
1. The complete code in Python that solves the problem.
2. A step-by-step explanation of how your code works and why it solves the problem correctly.
3. Any assumptions you made while solving the problem.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The provided code should be syntactically correct and run without errors.",
            "The code should solve the problem as specified in the instructions.",
            "The explanation should be clear, logical, and accurately describe how the code works."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

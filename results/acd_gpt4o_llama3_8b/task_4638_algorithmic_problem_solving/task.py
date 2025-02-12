class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem_statement": "Given a list of integers, find the longest increasing subsequence. The output should be the longest subsequence in the order they appear in the input list.",
                "example_input": [10, 9, 2, 5, 3, 7, 101, 18],
                "expected_output": [2, 3, 7, 101]
            },
            "2": {
                "problem_statement": "Given a list of integers, find the maximum subarray sum. The output should be the sum of the largest contiguous subarray.",
                "example_input": [-2, 1, -3, 4, -1, 2, 1, -5, 4],
                "expected_output": 6
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = """Solve the following algorithmic problem based on the given problem statement and example input:\n\nProblem Statement: {problem_statement}\nExample Input: {example_input}\n\nProvide your solution as a plain text string in the following format:\n\nSolution: [Your solution here]\n\nEnsure that your solution is correct, follows the algorithm described in the problem statement, and handles edge cases appropriately. Do not include any intermediate steps or explanations."""
        return instructions.format(problem_statement=t['problem_statement'], example_input=t['example_input'])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly implement the algorithm to solve the problem.",
            "The solution should be logically consistent and produce the expected output.",
            "The solution should handle edge cases appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

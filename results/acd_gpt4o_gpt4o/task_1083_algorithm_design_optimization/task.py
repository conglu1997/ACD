class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design an algorithm that finds the longest increasing subsequence in an array of integers. Optimize the algorithm for time complexity. The algorithm should have a time complexity of O(n log n) or better."},
            "2": {"problem": "Design an algorithm that detects and removes duplicate elements in a large dataset. Optimize the algorithm for space complexity. The algorithm should use only O(1) extra space."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design and optimize an algorithm to solve the following problem:

Problem:
{t['problem']}

Provide a detailed explanation of your algorithm, including the rationale behind your approach, and how you optimized it for the specified constraints (time or space complexity). Your response should include:
1. A clear description of the algorithm.
2. An explanation of the rationale behind your approach.
3. Details on how you optimized the algorithm for the specified constraint.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear description of the algorithm.",
            "The explanation should include the rationale behind the approach.",
            "The response should detail how the algorithm was optimized for the specified constraint."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

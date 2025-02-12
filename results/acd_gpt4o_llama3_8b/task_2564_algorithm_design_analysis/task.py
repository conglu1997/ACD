class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Given an array of integers, design an algorithm to find the maximum sum of any contiguous subarray."},
            "2": {"problem": "Design an algorithm to determine if a string has all unique characters without using additional data structures."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an algorithm to solve the following problem and analyze its time complexity:\n{t['problem']}\nSubmit your response in the following format:\nAlgorithm: [Your algorithm in plain text or pseudocode]\nTime Complexity: [Your analysis of the time complexity]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should correctly solve the problem.",
            "The time complexity analysis should be accurate.",
            "The response format should include both the algorithm and the time complexity analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

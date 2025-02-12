class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design an algorithm to find the longest increasing subsequence in an array of integers. Analyze its time and space complexity."
            },
            "2": {
                "problem": "Design an algorithm to solve the 0/1 knapsack problem using dynamic programming. Analyze its time and space complexity."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithm to solve the given computational problem and analyze its efficiency. Your response should include the algorithm in pseudocode and a detailed analysis of its time and space complexity. Ensure your solution is logically sound and efficient. Submit your response as a plain text string in the following format:\n\n1. Pseudocode:\n[Your pseudocode here]\n\n2. Complexity Analysis:\n[Your analysis here]\n\nProblem: {t['problem']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The algorithm should correctly solve the given problem.",
            "The time and space complexity analysis should be accurate.",
            "The pseudocode should be clear and follow standard conventions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

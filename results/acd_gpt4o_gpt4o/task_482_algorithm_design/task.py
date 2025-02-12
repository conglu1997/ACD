class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Design an algorithm to find the longest palindromic substring in a given string.", "constraints": "Your algorithm should be efficient in terms of time complexity."},
            "2": {"problem": "Optimize the algorithm for sorting an array of integers. Provide a detailed explanation of the optimization techniques used.", "constraints": "Your optimized algorithm should have a time complexity of O(n log n) or better."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        constraints = t["constraints"]
        instructions = f"""Your task is to design a novel algorithm to solve the following problem or optimize an existing one:

Problem: {problem}

Constraints: {constraints}

Provide a detailed explanation of your algorithm, including the steps involved, the logic behind it, and its time complexity. Ensure that your solution is clear, logical, and well-structured. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should address the problem effectively.",
            "The explanation should be clear, logical, and well-structured.",
            "The algorithm should meet the given constraints, including time complexity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

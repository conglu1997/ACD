class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Design an algorithm to find the greatest common divisor (GCD) of two integers using the Euclidean algorithm."
            },
            "2": {
                "problem": "Design an algorithm to sort an array of integers using the quicksort method."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a problem that requires designing an algorithm. Your task is to design an efficient algorithm to solve the problem and provide a detailed explanation of its steps and logic. Ensure that your explanation is clear and covers the reasoning behind each step.

Problem: {t['problem']}

Submit your algorithm design and explanation as a plain text string in the following format:

Algorithm Design: [Your algorithm design here]
Explanation: [Your explanation here]

Please follow this format strictly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm should correctly solve the given problem.",
            "The explanation should be clear and cover the reasoning behind each step.",
            "The algorithm should be efficient and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

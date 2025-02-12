class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Find all prime numbers up to a given number N.",
                "N": 100
            },
            "2": {
                "problem": "Calculate the greatest common divisor (GCD) of two given numbers.",
                "numbers": [48, 180]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following problem by generating an algorithm and explaining the steps involved in the solution:

Problem: {t['problem']}

For example, if the problem is to find all prime numbers up to a given number N, you should describe the algorithm you will use (e.g., the Sieve of Eratosthenes), implement the algorithm, and explain each step. Ensure that your explanation is clear and detailed.

Submit your response as a plain text string in the following format:

Algorithm:
[Your algorithm]

Explanation:
[Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The algorithm should correctly solve the given problem.",
            "The explanation should clearly describe the steps of the algorithm.",
            "The submission should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

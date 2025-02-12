class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "John has twice as many apples as Mary. If Mary has 5 apples, how many apples do John and Mary have together?"},
            "2": {"problem": "A train travels at a speed of 60 miles per hour. How long will it take to travel 180 miles?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following mathematical word problem by interpreting the given text and performing the necessary calculations. Provide your solution in plain text format.

Problem: {t['problem']}

Your response should include:
1. The interpreted mathematical equations or expressions.
2. The step-by-step calculations.
3. The final answer.

Provide your response in the format:
- Equations: [Your equations]
- Calculations: [Your step-by-step calculations]
- Answer: [Your final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly interpret the mathematical scenario described in the problem.",
            "The calculations should be accurate and correctly performed.",
            "The final answer should be correct based on the given problem.",
            "The response should include interpreted equations, step-by-step calculations, and the final answer."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

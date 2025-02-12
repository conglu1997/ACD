class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Jane has 3 times as many apples as Tom. If Tom has 5 apples and both of them together buy 12 more apples, how many apples do they have in total now?"},
            "2": {"problem": "A car travels 60 miles per hour. How far will it travel in 2.5 hours if it takes a 15-minute break after the first 1.5 hours?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to solve the following multi-step word problem:

Problem: {problem}

Your solution should include the following elements:
1. A clear explanation of each step needed to solve the problem.
2. The calculations performed at each step.
3. The final answer.

Provide your solution in the following format:

Step-by-step Explanation:
[Your explanation of each step]

Calculations:
[Your calculations for each step]

Final Answer:
[Your final answer]

Ensure your response is clear and detailed."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should include each step needed to solve the problem.",
            "The calculations performed at each step should be correct.",
            "The final answer should be correct and clearly stated."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A farmer has chickens and cows in his barn. The total number of animals is 30, and the total number of legs is 74. How many chickens and how many cows are there?"},
            "2": {"scenario": "Sophia is planning to buy some notebooks and pens. Each notebook costs $3 and each pen costs $2. If she wants to buy 5 items and spends exactly $12, how many notebooks and pens does she buy?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical word problem based on the given scenario:

Scenario:
{t['scenario']}

Provide a detailed solution to the problem, clearly showing all steps and calculations involved.

Submit your solution in the following format:

Solution:
1. [Step-by-step explanation]
2. [Final answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be logically correct.",
            "The solution should clearly show all steps and calculations involved.",
            "The final answer should correctly solve the problem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

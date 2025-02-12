class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A train travels 60 miles per hour and a car travels 40 miles per hour. They start from the same point and travel in opposite directions. After how many hours will they be 200 miles apart?"
            },
            "2": {
                "scenario": "John has twice as many apples as Mary. Together, they have 36 apples. How many apples does John have?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an algebraic word problem based on the following scenario and solve it:

Scenario: {t["scenario"]}

Your response should include the algebraic equations used to solve the problem and the final solution. Ensure your algebraic problem and solution are clearly articulated. Submit your response as a plain text string in the following format:

Problem: [Your algebraic word problem]
Solution: [Your solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a correctly formulated algebraic word problem.",
            "The response should include the correct algebraic equations and final solution."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

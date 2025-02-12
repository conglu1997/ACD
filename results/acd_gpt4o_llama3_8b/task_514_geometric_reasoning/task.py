class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Given a right-angled triangle with one leg measuring 3 units and the hypotenuse measuring 5 units, find the length of the other leg."
            },
            "2": {
                "problem": "A circle is inscribed in a square. If the area of the square is 16 square units, what is the radius of the circle?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following geometric problem and provide your solution with a clear explanation of the steps involved:

Problem: {t['problem']}

Submit your response as a plain text string in the format: 'Solution: [Your solution]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution must correctly answer the problem.",
            "The solution must include a clear explanation of the steps involved."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

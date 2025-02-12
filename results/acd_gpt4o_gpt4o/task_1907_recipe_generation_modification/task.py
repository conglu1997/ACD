class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a vegetarian pasta recipe that can be prepared in under 30 minutes.", "modification": "Modify the recipe to make it vegan while keeping the preparation time under 30 minutes."},
            "2": {"criteria": "Create a dessert recipe using chocolate and berries.", "modification": "Modify the recipe to make it gluten-free without changing the main ingredients."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a recipe based on the given criteria and then modify it according to the specified changes.

Criteria: {t['criteria']}

After generating the recipe, modify it as specified while adhering to the original constraints. Provide your response in plain text format with the following structure:

Original Recipe:
[Your original recipe here]

Modified Recipe:
[Your modified recipe here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The original recipe should meet the given criteria.",
            "The modified recipe should follow the specified changes and maintain the original constraints.",
            "Both recipes should be clear, coherent, and complete."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

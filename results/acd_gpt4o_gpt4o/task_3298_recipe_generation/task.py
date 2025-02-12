class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dish": "Spaghetti Carbonara"},
            "2": {"dish": "Vegetable Stir-Fry"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed step-by-step recipe for the following dish:

Dish: {t['dish']}

The recipe should include the following sections:
1. Ingredients: List all the ingredients needed, with quantities.
2. Preparation Steps: Describe any preparations required before cooking (e.g., chopping vegetables).
3. Cooking Instructions: Provide clear, step-by-step cooking instructions.
4. Estimated Cooking Time: Include an estimated total cooking time.
5. Serving Size: Specify the number of servings the recipe yields.

Ensure that the recipe is clear, easy to follow, and suitable for someone with basic cooking skills."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should include a complete list of ingredients with quantities.",
            "The preparation steps should be clear and logically ordered.",
            "The cooking instructions should be detailed and easy to follow.",
            "The recipe should include an estimated cooking time.",
            "The recipe should specify the serving size."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

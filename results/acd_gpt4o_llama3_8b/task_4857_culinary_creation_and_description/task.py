class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dish": "Spaghetti Carbonara", "ingredients": ["spaghetti", "eggs", "Parmesan cheese", "pancetta", "pepper", "salt"]},
            "2": {"criteria": "Create a dessert recipe that includes chocolate and berries."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "dish" in t:
            dish = t["dish"]
            ingredients = ", ".join(t["ingredients"])
            return f"""Describe the following dish in detail, including its taste, texture, appearance, and any cultural or historical significance if applicable. The dish is {dish}. It includes the following ingredients: {ingredients}. Ensure your description is vivid and captures the sensory experience of eating the dish. Submit your description as a plain text string."""
        else:
            criteria = t["criteria"]
            return f"""Create a recipe based on the following criteria: {criteria}. Ensure that the recipe is detailed, including the list of ingredients, step-by-step instructions for preparation, and a brief explanation of why the combination of ingredients was chosen. The recipe should be creative and follow the given criteria. Submit your recipe as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "dish" in t:
            criteria = ["The description should be vivid and capture the sensory experience of eating the dish.", "The description should include details about taste, texture, and appearance.", "The description should include any cultural or historical significance if applicable."]
        else:
            criteria = ["The recipe should be detailed and follow the given criteria.", "The recipe should include a list of ingredients and step-by-step instructions.", "The recipe should include a brief explanation of why the combination of ingredients was chosen.", "The recipe should be creative and feasible."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
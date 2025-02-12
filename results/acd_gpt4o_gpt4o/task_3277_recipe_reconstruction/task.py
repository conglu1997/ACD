class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["2 cups flour", "1 cup sugar", "1/2 cup butter", "2 eggs", "1 tsp baking powder", "1/2 cup milk"], "description": "A classic vanilla cake with a light and fluffy texture, perfect for birthdays and celebrations."},
            "2": {"ingredients": ["1 lb chicken breast", "1 cup rice", "1 bell pepper", "1 onion", "2 cloves garlic", "1 cup chicken broth", "1 tsp paprika", "1/2 tsp salt", "1/4 tsp black pepper"], "description": "A savory chicken and rice dish with a mix of colorful vegetables and a hint of paprika."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to reconstruct a recipe based on the given list of ingredients and the description of the final dish. Ensure that your recipe includes all necessary steps, is logically sequenced, detailed, and results in the described dish. Provide your response in the following format:\n\nIngredients: {', '.join(t['ingredients'])}\n\nDescription: {t['description']}\n\nRecipe:\n[Your recipe here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should include all the listed ingredients.",
            "The steps should be logically sequenced and comprehensive.",
            "The recipe should result in the described final dish.",
            "The recipe should be detailed and accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "broccoli", "rice", "soy sauce"], "servings": 4, "new_servings": 2},
            "2": {"ingredients": ["spaghetti", "tomato sauce", "ground beef", "parmesan cheese"], "servings": 6, "new_servings": 3}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = ', '.join(t['ingredients'])
        servings = t['servings']
        new_servings = t['new_servings']
        return f"""You are given a list of ingredients and a specified number of servings. Your task is to create a complete recipe using the given ingredients for the specified number of servings. After creating the recipe, convert the recipe to accommodate a different number of servings. Ensure that the recipe is clear, includes all necessary steps, and that the ingredient quantities are adjusted correctly for the new number of servings.

Ingredients: {ingredients}
Original Number of Servings: {servings}
New Number of Servings: {new_servings}

Submit your response as a plain text string in the following format:

Recipe for {servings} servings:
[Your recipe]

Recipe for {new_servings} servings:
[Converted recipe]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should include all given ingredients.",
            "The recipe should be clear and include all necessary steps.",
            "The ingredient quantities should be correctly adjusted for the new number of servings.",
            "The recipe should remain coherent and practical after conversion."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

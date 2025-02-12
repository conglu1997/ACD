class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": "chicken breast, garlic, lemon, olive oil, rosemary, salt, pepper",
                "context": "Recipe creation"
            },
            "2": {
                "recipe": "1. Preheat oven to 200°C. 2. Season the chicken breast with salt and pepper. 3. In a bowl, mix olive oil, lemon juice, and minced garlic. 4. Pour the mixture over the chicken. 5. Bake in the oven for 25 minutes.",
                "context": "Recipe comprehension"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'ingredients' in t:
            return f"You are required to create a detailed recipe using the following ingredients:\n\nIngredients: {t['ingredients']}\n\nEnsure that your recipe is clear, detailed, and includes all necessary steps and cooking times. Submit your recipe as a plain text string in the following format:\n\nRecipe: [Your detailed recipe here]"
        else:
            return f"You are required to identify any missing steps in the following recipe:\n\nRecipe: {t['recipe']}\n\nSubmit the missing steps as a plain text string in the following format:\n\nMissing Steps: [Your missing steps here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'ingredients' in t:
            validation_criteria = [
                "The response should be a coherent and detailed recipe using the given ingredients."]
        else:
            validation_criteria = [
                "The response should correctly identify any missing steps in the given recipe."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

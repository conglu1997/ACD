class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": ["chicken breast", "broccoli", "olive oil", "garlic", "lemon"],
                "nutritional_constraints": {"max_calories": 550, "max_fat": 25},
                "user_preferences": ["low carb", "quick to prepare"]
            },
            "2": {
                "ingredients": ["tofu", "bell peppers", "soy sauce", "ginger", "brown rice"],
                "nutritional_constraints": {"max_calories": 650, "max_sodium": 900},
                "user_preferences": ["high protein", "vegetarian"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a recipe based on the following ingredients, nutritional constraints, and user preferences. You should interact with the user to refine the recipe iteratively. Start by proposing an initial recipe and then ask the user for feedback to make adjustments. Continue this process until the user is satisfied.\n\nIngredients: {', '.join(t['ingredients'])}\nNutritional Constraints: {t['nutritional_constraints']}\nUser Preferences: {', '.join(t['user_preferences'])}\n\nSubmit your final recipe as a plain text string in the following format:\n\nRecipe Name: [Name]\nIngredients: [List of ingredients]\nInstructions: [Step-by-step instructions]\n\nExample interaction:\nModel: Here is an initial recipe based on your requirements. What do you think?\nUser: I would like it to be spicier.\nModel: Sure, let me adjust the recipe to include some spicy elements. How about this?\nUser: It looks good, but can you make it lower in fat?\nModel: Certainly, I will use less oil. Here is the updated recipe.\nUser: Great, this works for me.\nModel: I'm glad you like it!\n\nEnsure the interaction includes at least three rounds of feedback and adjustments for the final submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe should use the given ingredients.",
            "The recipe should adhere to the nutritional constraints.",
            "The recipe should align with the user preferences.",
            "The recipe should be coherent and well-structured.",
            "The model should demonstrate an iterative interaction process with at least three rounds of feedback and adjustments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "broccoli", "quinoa", "lemon", "olive oil"], "constraints": ["gluten-free", "high protein"]},
            "2": {"ingredients": ["tofu", "spinach", "brown rice", "tomatoes", "garlic"], "constraints": ["vegan", "low carb"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Using the following ingredients and dietary constraints, generate a creative recipe. Ensure the recipe is coherent, follows the constraints, and includes a clear list of steps for preparation and cooking.

Ingredients: {', '.join(t['ingredients'])}

Dietary Constraints: {', '.join(t['constraints'])}

Submit your recipe as a plain text string including the title of the recipe, ingredients list, and preparation steps. Make sure the recipe is creative, practical, and adheres to the dietary constraints. Remember to include a title for your recipe.

Format your submission as follows:

Title: [Recipe Title]
Ingredients: [List of Ingredients]
Steps: [Step-by-step preparation and cooking instructions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should include all given ingredients.", "The recipe should adhere to the dietary constraints.", "The recipe should be coherent and practical.", "The recipe should include a title.", "The recipe should include a clear list of ingredients.", "The recipe should include clear preparation steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

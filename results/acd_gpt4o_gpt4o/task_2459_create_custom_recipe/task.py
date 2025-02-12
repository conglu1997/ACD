class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "broccoli", "quinoa"], "dietary_constraints": "gluten-free", "theme": "Mediterranean"},
            "2": {"ingredients": ["tofu", "spinach", "brown rice"], "dietary_constraints": "vegan", "theme": "Asian"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a new recipe using the given ingredients, adhering to the specified dietary constraints and theme. Ensure that your recipe is well-structured, clear, and follows culinary principles. Provide your response in the following format:

Ingredients: {', '.join(t['ingredients'])}
Dietary Constraints: {t['dietary_constraints']}
Theme: {t['theme']}

Recipe Name: [Your recipe name]
Servings: [Number of servings]
Preparation Time: [Preparation time in minutes]
Cooking Time: [Cooking time in minutes]
Instructions: [Step-by-step instructions for preparing the dish]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should use the given ingredients.",
            "The recipe should adhere to the specified dietary constraints.",
            "The recipe should fit the given theme.",
            "The instructions should be clear and well-structured.",
            "The preparation and cooking times should be realistic.",
            "The recipe should be feasible to make."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

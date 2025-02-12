class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "spinach", "cream cheese", "garlic", "parmesan cheese"], "constraints": ["must be a main course", "must be baked", "prep time under 30 minutes", "should serve 2-4 people"]},
            "2": {"ingredients": ["tofu", "broccoli", "soy sauce", "ginger", "sesame seeds"], "constraints": ["must be vegan", "must be a stir-fry", "must be ready in under 20 minutes", "should serve 2-4 people"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = ', '.join(t["ingredients"])
        constraints = '; '.join(t["constraints"])
        return f"""Invent a new recipe based on the following ingredients and constraints:

Ingredients: {ingredients}
Constraints: {constraints}

Ensure the recipe is coherent, plausible, and follows the given constraints. Provide the recipe in the following format:

1. Title of the recipe
2. List of ingredients with reasonable quantities
3. Step-by-step preparation instructions

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should use the provided ingredients.", "The recipe should adhere to all given constraints.", "The recipe should be coherent and plausible.", "The quantities of ingredients should be reasonable and common."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

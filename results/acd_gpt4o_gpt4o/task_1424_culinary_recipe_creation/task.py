class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": "chicken breast, garlic, lemon, olive oil, rosemary", "constraints": "The recipe must be prepared in under 30 minutes and should be suitable for a low-carb diet.", "domain": "cooking"},
            "2": {"ingredients": "tofu, soy sauce, ginger, broccoli, sesame oil", "constraints": "The recipe must be vegan and should not include any added sugar.", "domain": "cooking"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = t["ingredients"]
        constraints = t["constraints"]
        domain = t["domain"]
        instructions = f"""Your task involves two parts:\n\n1. Recipe Creation: Based on the following ingredients and constraints, generate a cooking recipe.\n\nIngredients: {ingredients}\n\nConstraints: {constraints}\n\n2. Recipe Interpretation: Provide a detailed interpretation of the steps in your recipe, explaining why each step is important and how it contributes to the final dish.\n\nEnsure that your recipe is coherent, practical, and adheres to the given constraints. Your interpretation should demonstrate an understanding of the cooking process and the role of each ingredient.\n\nResponse Format:\nRecipe: <Your recipe>\nInterpretation: <Your interpretation>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should use all the given ingredients.",
            "The recipe should adhere to the given constraints.",
            "The recipe should be coherent and practical.",
            "The interpretation should explain the importance of each step and how it contributes to the final dish.",
            "The interpretation should demonstrate an understanding of the cooking process and the role of each ingredient."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

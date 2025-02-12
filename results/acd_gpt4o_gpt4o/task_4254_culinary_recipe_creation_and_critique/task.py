class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create_recipe", "dietary_restrictions": "vegan, gluten-free", "meal_type": "dinner", "ingredients_to_include": ["quinoa", "spinach", "mushrooms"], "additional_criteria": "The recipe should be nutritious and flavorful, suitable for a family of four."},
            "2": {"task": "critique_recipe", "recipe": "1 cup white rice, 2 cups water, 1 tbsp olive oil, 1/2 cup diced carrots, 1/2 cup peas, salt to taste", "criteria": "nutritional balance, flavor profile, ease of preparation"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "create_recipe":
            return f"Your task is to create a dinner recipe that adheres to the following dietary restrictions: {t['dietary_restrictions']}. Ensure the recipe includes the following ingredients: {', '.join(t['ingredients_to_include'])}. The recipe should be nutritious and flavorful, suitable for a family of four. Provide a detailed recipe, including the list of ingredients and step-by-step cooking instructions. Format your response as follows:\n\nIngredients:\n[List of ingredients]\n\nInstructions:\n[Step-by-step cooking instructions]"
        elif t["task"] == "critique_recipe":
            return f"Your task is to critique the following recipe: '{t['recipe']}'. Critique it based on the given criteria: {', '.join(t['criteria'])}. Provide a detailed critique, including suggestions for improvement regarding nutritional balance, flavor profile, and ease of preparation. Format your response as follows:\n\nCritique:\n1. Nutritional Balance: [Your analysis]\n2. Flavor Profile: [Your analysis]\n3. Ease of Preparation: [Your analysis]\n4. Suggestions for Improvement: [Your suggestions]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "create_recipe":
            criteria = [
                "The recipe should adhere to the given dietary restrictions.",
                "The recipe should include the specified ingredients.",
                "The recipe should be suitable for a family of four.",
                "The instructions should be clear and detailed.",
                "The recipe should be nutritious and flavorful."
            ]
        elif t["task"] == "critique_recipe":
            criteria = [
                "The critique should address nutritional balance, flavor profile, and ease of preparation.",
                "The suggestions for improvement should be practical and relevant.",
                "The critique should be detailed and coherent."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

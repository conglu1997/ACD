class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "garlic", "lemon", "thyme", "olive oil", "salt", "pepper"]},
            "2": {"ingredients": ["salmon fillet", "soy sauce", "ginger", "honey", "sesame oil", "green onions", "sesame seeds"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a recipe based on the following ingredients and provide detailed step-by-step instructions for cooking the dish:

Ingredients: {', '.join(t['ingredients'])}

Ensure that the recipe is creative, coherent, and practical. The instructions should be clear and easy to follow, and the recipe should be original. Provide your response in the following format:

Recipe Name: [Your recipe name]
Ingredients: [List of ingredients with quantities]
Instructions: [Step-by-step cooking instructions]

Example:
Recipe Name: Garlic Lemon Chicken
Ingredients:
- 2 chicken breasts
- 2 cloves garlic, minced
- 1 lemon, juiced
- 1 tbsp fresh thyme, chopped
- 2 tbsp olive oil
- Salt and pepper to taste

Instructions:
1. Preheat the oven to 375°F (190°C).
2. In a small bowl, mix the garlic, lemon juice, thyme, olive oil, salt, and pepper.
3. Place the chicken breasts in a baking dish and pour the mixture over them, ensuring they are well coated.
4. Bake in the preheated oven for 25-30 minutes or until the chicken is cooked through and no longer pink in the center.
5. Serve hot and enjoy!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should be based on the given ingredients.", "The instructions should be clear, coherent, and practical.", "The recipe should be original and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

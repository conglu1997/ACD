class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": ["chicken breast", "broccoli", "garlic", "soy sauce", "olive oil"],
                "meal_type": "dinner"
            },
            "2": {
                "recipe": "2 cups of cooked quinoa, 1 cup of black beans, 1/2 cup of corn, 1/4 cup of diced red onion, 1/4 cup of chopped cilantro, juice of 1 lime, salt and pepper to taste",
                "analysis_task": "nutritional breakdown"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "ingredients" in t:
            ingredients = ", ".join(t["ingredients"])
            meal_type = t["meal_type"]
            instructions = f"""Your task is to create a recipe for {meal_type} using the following ingredients: {ingredients}. Provide the recipe in plain text format, including a title, list of ingredients with measurements, and step-by-step instructions. Ensure the recipe is clear, coherent, and uses all the provided ingredients."""
        else:
            recipe = t["recipe"]
            analysis_task = t["analysis_task"]
            instructions = f"""Your task is to analyze the following recipe and provide a {analysis_task}. The analysis should include a breakdown of calories, protein, carbohydrates, and fats for the entire recipe. Provide your analysis in plain text format.

Recipe: {recipe}"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "ingredients" in t:
            criteria = [
                "The recipe should include all the given ingredients.",
                "The recipe should be clear and coherent.",
                "The recipe should be suitable for the specified meal type."
            ]
        else:
            criteria = [
                "The nutritional breakdown should include calories, protein, carbohydrates, and fats.",
                "The values provided should be reasonable and coherent for the given recipe."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

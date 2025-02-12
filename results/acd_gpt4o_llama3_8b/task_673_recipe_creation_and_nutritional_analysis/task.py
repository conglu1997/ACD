class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "vegetarian, high-protein, under 500 calories"},
            "2": {"constraints": "gluten-free, low-carb, under 300 calories"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        return f"""Create a recipe based on the following constraints: {constraints}. The recipe should include a list of ingredients and step-by-step instructions for preparation. Additionally, provide a nutritional analysis of the recipe, including the approximate calorie count and macronutrient breakdown (protein, carbohydrates, fats). Submit your response as a plain text string in the following format:

Recipe:
1. [ingredient]
2. [ingredient]
...

Instructions:
Step 1: [instruction]
Step 2: [instruction]
...

Nutritional Analysis:
Calories: [approximate calorie count]
Protein: [grams]
Carbohydrates: [grams]
Fats: [grams]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should adhere to the given constraints.",
            "The recipe should include a list of ingredients and step-by-step instructions for preparation.",
            "The nutritional analysis should include the approximate calorie count and macronutrient breakdown (protein, carbohydrates, fats)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

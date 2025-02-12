class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "Generate a recipe for a vegetarian lasagna. Ensure the recipe includes a list of ingredients, detailed step-by-step instructions, and nutritional information for each serving (calories, protein, fat, and carbohydrates)."
            },
            "2": {
                "task": "Modify the following recipe to make it suitable for a vegan diet. Original Recipe: \"Ingredients: 2 cups of milk, 3 eggs, 1 cup of sugar, 1 tablespoon of butter. Instructions: 1. Mix all ingredients in a bowl. 2. Bake at 350°F for 30 minutes.\" Ensure the modified recipe includes a list of ingredients, detailed step-by-step instructions, and nutritional information for each serving (calories, protein, fat, and carbohydrates)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Perform the following task:

{t['task']}

Ensure that the recipe you generate or modify includes:
1. A list of ingredients.
2. Detailed step-by-step instructions.
3. Logical sequencing and clarity in the steps.
4. Nutritional information for each serving (calories, protein, fat, and carbohydrates) presented as follows:
   - Calories: [value] kcal
   - Protein: [value] g
   - Fat: [value] g
   - Carbohydrates: [value] g

Submit your recipe as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe should include a clear list of ingredients.",
            "The recipe should provide detailed step-by-step instructions.",
            "The instructions should be logically sequenced and clear.",
            "The recipe should include nutritional information for each serving (calories, protein, fat, and carbohydrates) in the specified format.",
            "For Task 2, the modified recipe should be suitable for a vegan diet."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

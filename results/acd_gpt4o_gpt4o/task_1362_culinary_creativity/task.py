class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"cuisine": "Italian", "main_ingredient": "eggplant", "dietary_restriction": "vegan"},
            "2": {"cuisine": "Mexican", "main_ingredient": "chicken", "dietary_restriction": "gluten-free"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a unique recipe based on the following constraints:

Cuisine: {t['cuisine']}
Main Ingredient: {t['main_ingredient']}
Dietary Restriction: {t['dietary_restriction']}

Ensure that your recipe is coherent, follows the specified cuisine style, includes the main ingredient, and adheres to the dietary restriction. Provide your recipe in plain text format, including the ingredients list and the step-by-step instructions.

Format your response as follows:

Recipe Name: [Your recipe name]
Ingredients: [List of ingredients]
Instructions: [Step-by-step instructions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should be coherent.",
            "The recipe should follow the specified cuisine style.",
            "The recipe should include the main ingredient.",
            "The recipe should adhere to the dietary restriction.",
            "The recipe should include a list of ingredients.",
            "The recipe should include step-by-step instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

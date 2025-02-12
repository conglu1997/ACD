class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "recipe": "Classic Beef Lasagna",
                "dietary_restriction": "vegetarian"
            },
            "2": {
                "recipe": "Traditional Chocolate Cake",
                "dietary_restriction": "gluten-free"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Adapt the following recipe to meet the specified dietary restriction. Ensure that the adapted recipe maintains the original dish's flavor and texture as much as possible. Include a detailed list of ingredients and step-by-step instructions for preparing the adapted dish. Submit your adapted recipe as a plain text string.\n\nRecipe: {t['recipe']}\nDietary Restriction: {t['dietary_restriction']}\n\nFormat of submission:\nIngredients:\n[List of ingredients]\nInstructions:\n[Step-by-step instructions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The adapted recipe should meet the specified dietary restriction.",
            "The adapted recipe should maintain the original dish's flavor and texture as much as possible.",
            "The adapted recipe should include a detailed list of ingredients and step-by-step instructions for preparation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

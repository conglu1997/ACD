class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "vegan_gluten_free_dessert",
                "dietary_restrictions": "vegan, gluten-free",
                "meal_type": "dessert",
                "ingredients": ["coconut milk", "almond flour", "maple syrup"]
            },
            "2": {
                "task": "keto_breakfast",
                "dietary_restrictions": "keto",
                "meal_type": "breakfast",
                "ingredients": ["eggs", "avocado", "bacon"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            f"Your task is to generate a {t['meal_type']} recipe that adheres to the following dietary restrictions: {t['dietary_restrictions']}.\n"
            f"You must use the following ingredients: {', '.join(t['ingredients'])}.\n"
            "Ensure that the recipe is clear, detailed, and easy to follow. The recipe should include the following sections:\n"
            "1. Ingredients list with quantities\n"
            "2. Step-by-step instructions\n"
            "3. Serving size\n"
            "Provide the recipe in plain text format."
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe must adhere to the specified dietary restrictions.",
            "The recipe must use all the specified ingredients.",
            "The recipe must be clear, detailed, and easy to follow.",
            "The recipe must include sections for ingredients, instructions, and serving size."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
    
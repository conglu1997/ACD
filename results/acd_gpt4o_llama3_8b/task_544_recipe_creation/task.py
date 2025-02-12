class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "olive oil", "garlic", "lemon", "salt", "pepper", "rosemary"], "instructions": "Create a simple recipe using all the given ingredients. Ensure the recipe is easy to follow and includes all the necessary steps. Provide a title for the recipe and a brief description."},
            "2": {"ingredients": ["pasta", "tomato sauce", "basil", "parmesan cheese", "olive oil", "garlic", "salt", "pepper"], "instructions": "Create a simple recipe using all the given ingredients. Ensure the recipe is easy to follow and includes all the necessary steps. Provide a title for the recipe and a brief description."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a simple recipe using the following ingredients: {', '.join(t['ingredients'])}.\n{t['instructions']}\nFormat your response as follows:\nTitle: [Recipe Title]\nDescription: [Brief description]\nIngredients: [List of ingredients]\nInstructions: [Step-by-step instructions]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should use all the given ingredients.", "The recipe should be easy to follow and include all necessary steps.", "The recipe should be coherent and logical.", "The recipe should include a title and a brief description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

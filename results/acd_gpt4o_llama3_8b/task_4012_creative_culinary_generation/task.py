class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "ingredients": ["3 bananas", "2 cups of rice", "1 can of coconut milk", "1 tablespoon of curry powder"],
                "instructions": "Using the provided ingredients, create a detailed recipe for a main course dish. Ensure the recipe includes clear steps and incorporates all the ingredients. Submit your response as a plain text string in the following format: 'Recipe: [Your recipe]'. No additional ingredients should be used."
            },
            "2": {
                "ingredients": ["2 carrots", "1 cup of quinoa", "1 avocado", "1 lemon", "1 teaspoon of cumin"],
                "instructions": "Using the provided ingredients, create a detailed recipe for a main course dish. Ensure the recipe includes clear steps and incorporates all the ingredients. Submit your response as a plain text string in the following format: 'Recipe: [Your recipe]'. No additional ingredients should be used."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"{t['instructions']}\n\nIngredients:\n" + "\n".join([f"- {ingredient}" for ingredient in t['ingredients']])

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The recipe must include all provided ingredients.",
            "The steps should be clear and logically structured.",
            "The recipe should be feasible and practical for cooking.",
            "The recipe should not use any ingredients beyond the provided ones.",
            "The recipe should demonstrate creativity in combining the ingredients." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

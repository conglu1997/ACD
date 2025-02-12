class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": {
                    "cuisine": "Italian",
                    "main_ingredient": "chicken",
                    "dietary_restrictions": ["gluten-free"],
                    "servings": 4,
                    "dish_type": "main course"
                },
                "instructions": "Generate a gluten-free Italian recipe that uses chicken as the main ingredient. The recipe should be for 4 servings and should be a main course. Explain the reasoning behind your choice of ingredients and the steps in the recipe. Submit your response as a plain text string with two sections: 'Recipe' and 'Explanation'."
            },
            "2": {
                "constraints": {
                    "cuisine": "Mexican",
                    "main_ingredient": "tofu",
                    "dietary_restrictions": ["vegan"],
                    "servings": 2,
                    "dish_type": "appetizer"
                },
                "instructions": "Generate a vegan Mexican recipe that uses tofu as the main ingredient. The recipe should be for 2 servings and should be an appetizer. Explain the reasoning behind your choice of ingredients and the steps in the recipe. Submit your response as a plain text string with two sections: 'Recipe' and 'Explanation'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a {t['constraints']['dietary_restrictions'][0]} {t['constraints']['cuisine']} recipe that uses {t['constraints']['main_ingredient']} as the main ingredient. The recipe should be for {t['constraints']['servings']} servings and should be a {t['constraints']['dish_type']}. Explain the reasoning behind your choice of ingredients and the steps in the recipe. Submit your response as a plain text string with two sections: 'Recipe' and 'Explanation'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include a valid recipe that conforms to the given constraints.",
            "The recipe should be clear and follow a logical sequence.",
            "The explanation should clearly describe the reasoning behind the choice of ingredients and the steps in the recipe."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

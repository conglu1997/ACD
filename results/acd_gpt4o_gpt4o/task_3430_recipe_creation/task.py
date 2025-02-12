class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dietary_restrictions": "Vegan, gluten-free",
                "ingredients": ["quinoa", "spinach", "chickpeas", "tomatoes", "avocado", "lemon", "olive oil"]
            },
            "2": {
                "dietary_restrictions": "Keto, dairy-free",
                "ingredients": ["cauliflower", "chicken breast", "broccoli", "olive oil", "garlic", "almond flour", "basil"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            "Your task is to generate a new recipe based on the given dietary restrictions and available ingredients. "
            "Ensure that the recipe adheres to the dietary restrictions and makes use of the provided ingredients. "
            "Provide a detailed recipe, including the following elements: \n\n"
            "1. Recipe Name \n"
            "2. Ingredients List \n"
            "3. Step-by-step Instructions \n"
            "4. Estimated Cooking Time \n"
            "5. Serving Size \n"
            "6. Justification for how the recipe meets the dietary restrictions"
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should adhere to the given dietary restrictions.",
            "The recipe should include all the provided ingredients.",
            "The step-by-step instructions should be clear and detailed.",
            "The justification should explain how the recipe meets the dietary restrictions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"recipe": [
                "Preheat the oven to 350 degrees Fahrenheit.",
                "In a bowl, mix 2 cups of flour, 1 cup of sugar, and a teaspoon of baking powder.",
                "Add 2 eggs and a cup of milk to the dry ingredients and stir until smooth.",
                "Pour the mixture into a greased baking pan.",
                "Bake for 25 minutes or until a toothpick inserted into the center comes out clean.",
                "Let the cake cool before serving."
            ]},
            "2": {"recipe": [
                "Boil 4 cups of water in a pot.",
                "Add 200 grams of pasta and a pinch of salt to the boiling water.",
                "Cook the pasta for 10-12 minutes, stirring occasionally.",
                "Drain the water and set the pasta aside.",
                "In a separate pan, heat 2 tablespoons of olive oil over medium heat.",
                "Add a diced onion and 2 cloves of minced garlic to the pan and sauté for 5 minutes.",
                "Add a can of diced tomatoes and a teaspoon of dried basil to the pan and cook for another 5 minutes.",
                "Mix the cooked pasta with the sauce and serve hot."
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to follow the given recipe and provide the final step-by-step instructions and the expected outcome. Make sure to list the steps in the correct order and describe the final product.

Recipe:
{chr(10).join(t['recipe'])}

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should list all the steps in the correct order.",
            "The response should accurately describe the final product.",
            "The response should be clear and easy to follow."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "base_recipe": "Classic Italian Lasagna",
                "constraints": "Make it vegetarian and gluten-free.",
                "theme": "Mediterranean"
            },
            "2": {
                "base_recipe": "Beef Wellington",
                "constraints": "Use a plant-based meat substitute and make it suitable for a festive occasion.",
                "theme": "Holiday Feast"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a base recipe and a set of constraints and themes. Your task is to generate a modified version of the recipe that adheres to the given constraints while maintaining the core essence of the dish. Ensure that the modified recipe is clear, logically structured, and includes all necessary steps and ingredients.

Base Recipe: {t['base_recipe']}

Constraints: {t['constraints']}
Theme: {t['theme']}

Your response should include:
1. An explanation of how you modified the base recipe to meet the constraints and theme.
2. The full modified recipe, including ingredients and step-by-step instructions.

Example:
Explanation: Adjustments were made to the base recipe to fit the constraints and theme without altering the essence of the dish.

Modified Recipe:
Ingredients:
- [List of ingredients]

Instructions:
1. [Step-by-step instructions]

Submit your response as a plain text string in the following format:
Explanation: [Your explanation]
Modified Recipe: [Your modified recipe]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should clearly describe how the base recipe was modified to meet the constraints and theme.",
            "The modified recipe should be clear, logically structured, and include all necessary steps and ingredients."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

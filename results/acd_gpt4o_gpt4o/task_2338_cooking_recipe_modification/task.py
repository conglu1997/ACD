class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "recipe": "Spaghetti Carbonara: 200g spaghetti, 100g pancetta, 2 large eggs, 50g pecorino cheese, 50g parmesan, 2 cloves garlic, 1 tbsp olive oil, salt, and pepper.",
                "modification": "Make this recipe vegetarian without using any meat substitutes."},
            "2": {
                "recipe": "Chicken Stir Fry: 200g chicken breast, 1 bell pepper, 1 carrot, 100g broccoli, 2 tbsp soy sauce, 1 tbsp sesame oil, 2 cloves garlic, 1 tsp ginger, salt, and pepper.",
                "modification": "Modify this recipe to be gluten-free."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to modify the following cooking recipe to meet the specified dietary restrictions or preferences.

Recipe: {t['recipe']}

Modification: {t['modification']}

Provide the modified recipe in plain text format with a clear explanation of the changes you made and why. Format your response as follows:
Modified Recipe: <your modified recipe>
Explanation: <your explanation>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The modified recipe should adhere to the specified dietary restriction or preference.",
            "The explanation should clearly describe the changes made and the reasoning behind them.",
            "The modified recipe should still be practical and coherent for cooking.",
            "The modified recipe should maintain the essence and flavor profile of the original dish."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

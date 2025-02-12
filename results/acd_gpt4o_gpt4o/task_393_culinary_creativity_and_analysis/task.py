class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "create", "ingredients": ["chicken breast", "garlic", "lemon", "thyme", "olive oil"]},
            "2": {"task": "analyze", "recipe": "Spaghetti Carbonara: Ingredients: Spaghetti, eggs, pancetta, Parmesan cheese, black pepper. Instructions: Cook the spaghetti. Fry the pancetta until crispy. Beat the eggs and mix with grated Parmesan. Combine everything and season with black pepper."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "create":
            return f"Your task is to create a recipe using the following ingredients: {', '.join(t['ingredients'])}. Provide the recipe with detailed instructions, including cooking times and techniques. Ensure the recipe is original and feasible to cook."
        elif t["task"] == "analyze":
            return f"Your task is to analyze the following recipe for Spaghetti Carbonara and suggest improvements. The recipe is: {t['recipe']} Provide your analysis and suggestions for improvement in a clear and detailed manner."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "create":
            criteria = [
                "The recipe should use all the given ingredients.",
                "The recipe should include detailed instructions.",
                "The recipe should be original and feasible to cook."
            ]
        elif t["task"] == "analyze":
            criteria = [
                "The analysis should be clear and detailed.",
                "The suggestions for improvement should be practical and enhance the recipe."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

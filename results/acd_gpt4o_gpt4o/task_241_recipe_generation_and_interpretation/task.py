class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken", "rice", "broccoli", "soy sauce"], "constraints": ["must be a one-pot meal", "must serve 4 people"], "expected_result": "A coherent recipe that meets the constraints"},
            "2": {"recipe": "1. Preheat oven to 375°F. 2. Mix 2 cups of flour, 1 cup of sugar, and 1 tsp of baking soda. 3. Add 2 eggs and 1 cup of milk. 4. Pour batter into a greased pan. 5. Bake for 25 minutes.", "questions": ["What temperature should the oven be set to?", "How long should the batter be baked?", "How many cups of flour are needed?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "ingredients" in t:
            return f"""Create a recipe using the following ingredients and constraints:

Ingredients: {', '.join(t['ingredients'])}
Constraints: {', '.join(t['constraints'])}

Provide the recipe in a clear, step-by-step format, ensuring it adheres to the given constraints. The format should include:
1. A list of ingredients with quantities
2. Step-by-step cooking instructions
3. Serving information
"""
        else:
            return f"""Interpret the following recipe and answer the questions below:

Recipe: {t['recipe']}

Questions: {', '.join(t['questions'])}

Provide your answers in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "ingredients" in t:
            criteria = ["The recipe should be coherent, follow the given constraints, and be in the specified format."]
        else:
            criteria = ["The answers should be correct based on the provided recipe."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

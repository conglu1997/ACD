class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Create a dessert recipe that includes chocolate, nuts, and a tropical fruit."},
            "2": {"constraints": "Create a vegetarian main course recipe that includes quinoa, spinach, and a dairy-free cheese substitute."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed recipe based on the following constraints:

Constraints: {t['constraints']}

Your recipe should include:
1. A list of ingredients with precise measurements.
2. Step-by-step instructions for preparing the dish.
3. An explanation of the key culinary techniques used in the recipe.

Ensure your recipe is clear, accurate, and feasible to follow. Provide your response in plain text format. Label each section clearly as 'Ingredients', 'Instructions', and 'Culinary Techniques'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should include the specified ingredients and adhere to the given constraints.", "The explanation of culinary techniques should be correct and relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

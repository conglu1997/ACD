class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "constraints": "Create a vegan dessert recipe that includes chocolate and uses no refined sugar."},
            "2": {"task_type": "interpret", "recipe": """Chocolate Avocado Mousse:

Ingredients:
- 2 ripe avocados
- 1/2 cup cocoa powder
- 1/4 cup maple syrup
- 1 tsp vanilla extract
- A pinch of salt

Instructions:
1. Cut the avocados in half, remove the pits, and scoop the flesh into a blender.
2. Add the cocoa powder, maple syrup, vanilla extract, and salt to the blender.
3. Blend until smooth and creamy.
4. Transfer the mousse to serving bowls and refrigerate for at least 30 minutes before serving."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to generate a recipe based on the following constraints:\n\nConstraints: {t['constraints']}\n\nEnsure that the recipe is complete, follows the given constraints, and is easy to follow. Provide your recipe in plain text format. Your response should be structured as follows:\n\n- Recipe Name\n- Ingredients: [list of ingredients]\n- Instructions: [detailed step-by-step instructions]"""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following recipe and explain each step in detail:\n\nRecipe:\n{t['recipe']}\n\nFor each step, provide a detailed explanation of what needs to be done, including any tips or important considerations. Ensure your explanations are clear and comprehensive, capturing all necessary details for someone to successfully follow the recipe. Provide your explanations in plain text format, numbered to correspond with the steps."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The recipe should be vegan, include chocolate, and use no refined sugar.", "The recipe should be clear and easy to follow."]
        elif t['task_type'] == 'interpret':
            criteria = ["The explanations should accurately and comprehensively detail the steps in the recipe."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

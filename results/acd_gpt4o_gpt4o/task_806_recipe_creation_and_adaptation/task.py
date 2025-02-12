class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a vegetarian pasta dish that includes tomatoes, spinach, and cheese. The recipe should serve 4 people.", "task_type": "create"},
            "2": {"recipe": "Chicken Alfredo: Ingredients: 1 lb chicken breast, 1 lb fettuccine, 2 cups heavy cream, 1 cup Parmesan cheese, 2 cloves garlic, salt, pepper. Instructions: Cook the fettuccine according to package instructions. In a separate pan, cook the chicken until browned and cooked through. Add garlic and cook for another minute. Add heavy cream and Parmesan cheese, and cook until the sauce thickens. Combine with the pasta and season with salt and pepper.", "adaptation": "Make this recipe suitable for a lactose-intolerant person while keeping it flavorful. Consider using alternative ingredients that do not compromise on taste.", "task_type": "adapt"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'create':
            return f"""Your task is to create a new recipe based on the following criteria: {t['criteria']}. Ensure that your recipe is clear, detailed, and includes the necessary ingredients and steps to serve 4 people. Provide your recipe in the following format:

Title: [Title of the dish]
Ingredients: [List of ingredients with quantities]
Instructions: [Step-by-step instructions]"""
        elif t['task_type'] == 'adapt':
            return f"""Your task is to adapt the following recipe to meet new requirements: {t['recipe']}. The adaptation requirement is: {t['adaptation']}. Ensure that your adapted recipe is clear, detailed, and maintains the flavor while accommodating the new requirement. Provide your adapted recipe in the following format:

Title: [Title of the dish]
Ingredients: [List of ingredients with quantities]
Instructions: [Step-by-step instructions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'create':
            criteria = ["The recipe should be clear and detailed.", "The recipe should include the necessary ingredients and steps to serve 4 people.", "The recipe should be a vegetarian pasta dish including tomatoes, spinach, and cheese."]
        elif t['task_type'] == 'adapt':
            criteria = ["The adapted recipe should be clear and detailed.", "The adapted recipe should include alternative ingredients suitable for a lactose-intolerant person.", "The adapted recipe should maintain the flavor of the original dish."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

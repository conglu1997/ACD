class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken", "garlic", "lemon"], "cuisine": "Italian", "dietary": "gluten-free"},
            "2": {"ingredients": ["tofu", "soy sauce", "ginger"], "cuisine": "Asian", "dietary": "vegan"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed recipe using the following constraints:

Ingredients: {', '.join(t['ingredients'])}
Cuisine Type: {t['cuisine']}
Dietary Requirements: {t['dietary']}

Ensure your recipe includes the following sections:

1. Title: [Recipe Title]
2. Ingredients: [List all ingredients with measurements]
3. Instructions: [Step-by-step cooking instructions]
4. Dietary Information: [Explain how the recipe meets the dietary requirements]

Example Format:
Title: [Your Recipe Title]
Ingredients: [List of ingredients with measurements]
Instructions: [Detailed, step-by-step instructions]
Dietary Information: [Explanation of dietary compliance]

Your recipe should be clear, logically organized, and suitable for someone with basic cooking skills. Submit your recipe as a plain text string in the following format:

Title: [Your Recipe Title]
Ingredients: [List of ingredients with measurements]
Instructions: [Detailed, step-by-step instructions]
Dietary Information: [Explanation of dietary compliance]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should use all the specified ingredients.",
            "The recipe should follow the given cuisine type.",
            "The recipe should meet the stated dietary requirements.",
            "The recipe should be clear and logically organized."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

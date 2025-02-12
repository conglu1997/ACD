class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "lemon", "garlic", "olive oil", "rosemary"], "constraints": ["must be a main course", "prep time under 30 minutes"]},
            "2": {"ingredients": ["tofu", "soy sauce", "ginger", "broccoli", "sesame oil"], "constraints": ["must be vegan", "serve at least 2 people"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a recipe based on the given ingredients and constraints. Ensure that the recipe is coherent, follows a logical sequence, and adheres to the constraints provided. Additionally, explain the reasoning behind your choices, such as why certain ingredients are used together or specific cooking techniques are chosen.

Ingredients: {', '.join(t['ingredients'])}

Constraints: {', '.join(t['constraints'])}

Instructions:
1. List the ingredients and their quantities.
2. Provide step-by-step instructions for preparing the dish.
3. Explain the reasoning behind your choices.

Your response should be in the following format:
Recipe:
[Your recipe]

Explanation:
[Your explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should be coherent and follow a logical sequence.", "The recipe should adhere to the constraints provided.", "The explanation should clearly justify the choices made."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

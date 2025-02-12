class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": ["chicken breast", "broccoli", "rice", "soy sauce", "garlic"], "constraints": "The recipe should be suitable for a low-sodium diet."},
            "2": {"ingredients": ["salmon", "spinach", "quinoa", "lemon", "dill"], "constraints": "The recipe should be ready in under 30 minutes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = ', '.join(t['ingredients'])
        constraints = t['constraints']
        return f"""Generate a detailed cooking recipe using the following ingredients: {ingredients}. Ensure that the recipe adheres to the following constraints: {constraints}.

Your response should include:
1. A list of the required ingredients with quantities.
2. Step-by-step cooking instructions.

Submit your response as a plain text string in the following format:

Ingredients:
- Ingredient 1: Quantity
- Ingredient 2: Quantity
...

Instructions:
1. Step 1
2. Step 2
...

Example:
Ingredients:
- Chicken breast: 200 grams
- Broccoli: 1 cup
...

Instructions:
1. Preheat the oven to 180°C.
2. Season the chicken breast with garlic and soy sauce...
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should use all the provided ingredients.",
            "The recipe should adhere to the specified constraints.",
            "The instructions should be clear, coherent, and logically sequenced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

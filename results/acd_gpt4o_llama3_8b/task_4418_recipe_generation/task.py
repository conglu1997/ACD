class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dish": "vegan lasagna", "special_requirements": "gluten-free, nut-free"},
            "2": {"dish": "chocolate cake", "special_requirements": "sugar-free, dairy-free"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dish = t['dish']
        special_requirements = t['special_requirements']
        return f"""You are tasked with generating a detailed recipe for the following dish: {dish}. The recipe must meet the following special requirements: {special_requirements}. Your recipe should include the following sections:

1. Ingredients: A list of all ingredients with quantities.
2. Instructions: Step-by-step instructions for preparing the dish.
3. Special Notes: Any additional tips or substitutions related to the special requirements.

Ensure your recipe is clear, precise, and logically structured. Submit your response in the following format:

Recipe for {dish}:

Ingredients:
- Ingredient 1: Quantity
- Ingredient 2: Quantity
...

Instructions:
1. Instruction step 1
2. Instruction step 2
...

Special Notes:
- Note 1
- Note 2
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should include a complete list of ingredients with quantities.",
            "The instructions should be clear, precise, and logically structured.",
            "The recipe should meet the specified special requirements.",
            "The recipe should include special notes or substitutions related to the special requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dish_name": "Dragonfruit Delight", "description": "A mystical dessert that combines the sweetness of dragonfruit with the crunchiness of enchanted almonds."},
            "2": {"dish_name": "Phoenix Flame Stew", "description": "A spicy stew that is said to rejuvenate the eater, made from the mythical phoenix's flame peppers."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed recipe for the following fictional dish: '{t["dish_name"]}'. The recipe should include:
1. A list of ingredients with quantities.
2. Step-by-step instructions for preparing the dish.
3. A brief description of the dish, including its mythical or fictional background.

Ensure that the recipe is coherent, creative, and follows a logical sequence. Submit your recipe as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should include a list of ingredients with quantities.", "The recipe should include step-by-step instructions for preparation.", "The recipe should include a brief description of the dish and its fictional background.", "The recipe should be coherent and creative."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

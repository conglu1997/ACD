class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dietary_restriction": "vegan", "meal_type": "dinner"},
            "2": {"dietary_restriction": "gluten-free", "meal_type": "dessert"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dietary_restriction = t["dietary_restriction"]
        meal_type = t["meal_type"]
        return f"""Generate a recipe for a {meal_type} that adheres to the following dietary restriction: {dietary_restriction}. Ensure that the recipe is complete, with a list of ingredients and step-by-step instructions for preparation. The recipe should be practical, easy to follow, and should not include any ingredients that violate the dietary restriction. Submit your recipe as a plain text string in the following format:

Ingredients:
[list of ingredients]

Instructions:
[list of step-by-step instructions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should be complete with a list of ingredients and step-by-step instructions.",
            "The recipe should adhere to the specified dietary restriction.",
            "The recipe should be practical and easy to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

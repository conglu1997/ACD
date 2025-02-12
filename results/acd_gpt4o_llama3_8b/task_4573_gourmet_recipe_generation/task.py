class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Create a gourmet dessert that includes chocolate, berries, and a crunchy element. The recipe should be suitable for a fine dining experience and include at least three different components (e.g., mousse, crumble, and sauce)."},
            "2": {"criteria": "Create a vegetarian main course that includes a protein-rich ingredient, seasonal vegetables, and a unique sauce. The recipe should be sophisticated enough for a high-end restaurant and include at least three different components (e.g., roasted vegetables, grain, and sauce)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        criteria = t["criteria"]
        return f"""Generate a detailed recipe for a gourmet dish based on the following criteria. Ensure that the recipe is both creative and practically feasible for a fine dining experience. Include a list of ingredients and step-by-step instructions for preparing each component.

Criteria: {criteria}

Submit your recipe as a plain text string in the following format:

Recipe Name: [Name of the dish]
Ingredients:
- [List of ingredients]
Instructions:
1. [Step-by-step instructions for each component]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recipe should be creative.",
            "The recipe should be practically feasible.",
            "The recipe should include a list of ingredients and step-by-step instructions.",
            "The recipe should meet the given criteria for the dish."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

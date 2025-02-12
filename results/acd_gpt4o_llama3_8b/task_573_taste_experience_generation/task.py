class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"ingredients": "lemon, honey, ginger", "context": "a soothing herbal tea on a cold winter night"},
            "2": {"ingredients": "chocolate, chili pepper, cinnamon", "context": "a rich and spicy dessert at a festive dinner party"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        ingredients = t['ingredients']
        context = t['context']
        return f"""Based on the following ingredients and context, generate a detailed description of the taste experience:

Ingredients: {ingredients}
Context: {context}

Ensure that your description is vivid, evocative, and captures the sensory experience of taste. The description should be between 50 to 150 words. Submit your description as a plain text string.

Example Ingredients: strawberries, balsamic vinegar, mint
Example Context: a refreshing summer salad
Example Description: The tangy sweetness of ripe strawberries mingles with the sharp acidity of balsamic vinegar, creating a delightful contrast. The fresh mint leaves add a cool, refreshing note, making each bite a burst of summer flavors."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

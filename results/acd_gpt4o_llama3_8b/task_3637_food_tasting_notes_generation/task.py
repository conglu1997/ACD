class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"food_item": "chocolate cake"},
            "2": {"food_item": "spicy ramen"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        food_item = t["food_item"]
        return f"""Generate detailed tasting notes for the following food item: {food_item}. Your notes should describe the flavor, texture, aroma, and overall experience of eating the food. Use evocative and sensory-rich language to convey the experience to someone who has never tried it before. Submit your response as a plain text string in the following format:

Tasting Notes:
[Your tasting notes here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The tasting notes should describe the flavor, texture, aroma, and overall experience of the food item.",
            "The language should be evocative and sensory-rich.",
            "The notes should be detailed and specific to the given food item."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

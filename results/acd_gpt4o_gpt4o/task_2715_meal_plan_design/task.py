class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"preferences": "vegetarian", "requirements": "high protein, low sugar"},
            "2": {"preferences": "low carb", "requirements": "gluten-free, dairy-free"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design a balanced meal plan based on the given dietary preferences and requirements. Ensure that the meal plan is nutritious, varied, and appealing. Provide a detailed description of each meal, including ingredients and preparation instructions. Your response should be in plain text format.

Preferences: {t['preferences']}
Requirements: {t['requirements']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The meal plan should align with the given dietary preferences and requirements.",
            "The meal plan should be balanced and nutritious.",
            "The meal descriptions should be detailed and include ingredients and preparation instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

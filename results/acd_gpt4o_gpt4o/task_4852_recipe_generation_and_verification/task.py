class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dish": "Chocolate Chip Cookies"},
            "2": {"dish": "Vegetarian Lasagna"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed recipe for the following dish. Ensure that your recipe is clear, accurate, and easy to follow. Additionally, explain the rationale behind each step to help the reader understand why it is necessary.

Dish: {t['dish']}

Your response should include:
1. A list of required ingredients and their quantities.
2. Detailed, step-by-step instructions.
3. An explanation of the rationale behind each step.

Ensure that the explanations for each step are detailed and that the steps are logically ordered.

Provide your recipe and explanations in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The recipe should be clear and detailed.", "The rationale behind each step should be explained.", "The steps should be logically ordered.", "The recipe should be feasible to follow."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

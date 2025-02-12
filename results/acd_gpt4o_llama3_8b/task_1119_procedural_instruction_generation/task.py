class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "activity": "Baking a chocolate cake"
            },
            "2": {
                "activity": "Assembling a flat-pack bookshelf"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed step-by-step guide for performing the following activity:

Activity: {t['activity']}

Your guide should be clear and concise, include all necessary steps and materials, and avoid common pitfalls. Submit your guide as a plain text string in the format 'Step 1: [First step]. Step 2: [Second step], ...'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The guide is clear and concise.",
            "The guide includes all necessary steps and materials.",
            "The guide avoids common pitfalls relevant to the activity."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

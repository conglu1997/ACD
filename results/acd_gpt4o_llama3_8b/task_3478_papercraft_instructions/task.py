class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "model": "Origami Crane",
                "materials": "A square piece of paper"
            },
            "2": {
                "model": "Paper Airplane",
                "materials": "A rectangular piece of paper"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate step-by-step instructions to create the following papercraft model:

Model: {t['model']}
Materials: {t['materials']}

Your instructions should be clear and detailed, guiding the user through each step of the process. Ensure that your instructions are logically sequenced and easy to follow. Use plain text format and number each step. Here is an example structure:

1. Fold the paper in half horizontally.
2. Unfold the paper and fold it in half vertically.
3. Unfold the paper and fold each corner to the center of the paper.

Continue this pattern until the papercraft model is complete. Ensure that each step is concise and includes necessary details for accuracy. For example, instead of saying 'fold the paper,' specify 'fold the top left corner to meet the bottom right corner.' Submit your instructions as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The instructions should be logically sequenced and easy to follow.",
            "Each step should be concise and include necessary details for accuracy.",
            "The final instructions should accurately describe how to create the specified papercraft model.",
            "The submission should be in plain text format and numbered appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

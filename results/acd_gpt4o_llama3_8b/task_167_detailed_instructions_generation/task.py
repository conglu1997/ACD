class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "How to bake a chocolate cake from scratch."
            },
            "2": {
                "task_description": "How to change a flat tire on a car."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate detailed step-by-step instructions for performing the following task: {t['task_description']}. Ensure the instructions are clear, logically ordered, and cover all necessary steps from start to finish. Submit your instructions as a plain text string with each step on a new line.

Example format:
1. [First step]
2. [Second step]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The instructions should be clear and easy to follow.", "The steps should be logically ordered.", "The instructions should cover all necessary steps from start to finish."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

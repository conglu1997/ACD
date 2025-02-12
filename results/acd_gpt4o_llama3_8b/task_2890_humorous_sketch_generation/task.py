class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a humorous sketch based on the following scenario: A cat trying to catch a laser pointer but getting tangled in yarn instead.",
                "task_type": "sketch_generation"
            },
            "2": {
                "description": "Interpret the humor in the following sketch: A dog reading a newspaper with the headline 'Cat Wins Nobel Prize'. Describe why this is funny in a detailed manner.",
                "task_type": "sketch_interpretation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'sketch_generation':
            return f"""Generate a humorous sketch based on the following scenario. Describe the sketch in detail, including the setting, characters, and actions that make it funny. Submit your description as a plain text string.

Scenario:
{t['description']}

Your description should be at least 100 words long."""
        elif t['task_type'] == 'sketch_interpretation':
            return f"""Interpret the humor in the following sketch. Describe why it is funny in a detailed manner. Submit your explanation as a plain text string.

Sketch Description:
{t['description']}

Your explanation should be at least 100 words long."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'sketch_generation':
            validation_criteria = [
                "The sketch should be humorous and creatively depict the given scenario.",
                "The description should be detailed and clearly convey the visual elements of the sketch.",
                "The description should be at least 100 words long."
            ]
        elif t['task_type'] == 'sketch_interpretation':
            validation_criteria = [
                "The interpretation should clearly explain why the sketch is funny.",
                "The explanation should be detailed and demonstrate an understanding of visual humor.",
                "The explanation should be at least 100 words long."
            ]
        else:
            validation_criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

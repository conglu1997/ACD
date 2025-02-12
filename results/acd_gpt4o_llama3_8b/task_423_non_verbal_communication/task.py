class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A person is standing with their arms crossed, their eyebrows are furrowed, and their lips are pressed into a thin line. They are tapping their foot rapidly.",
                "task_type": "interpretation"
            },
            "2": {
                "scenario": "A student is sitting in a classroom, listening to a lecture. Describe their body language, facial expressions, and gestures to indicate that they are bored and disinterested.",
                "task_type": "generation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpretation':
            return f"""Interpret the following description of body language, facial expressions, and gestures. Infer the emotions or intentions of the person described. Submit your interpretation as a plain text string.

Description:
{t['description']}"""
        elif t['task_type'] == 'generation':
            return f"""Generate a detailed description of body language, facial expressions, and gestures for the given scenario. Ensure that your description accurately reflects the specified emotions or intentions. Submit your description as a plain text string.

Scenario:
{t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpretation':
            validation_criteria = [
                "The interpretation should accurately infer the emotions or intentions of the person described.",
                "The interpretation should be coherent and logically follow from the description."
            ]
        elif t['task_type'] == 'generation':
            validation_criteria = [
                "The generated description should accurately reflect the specified emotions or intentions.",
                "The description should be detailed and use appropriate body language, facial expressions, and gestures."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

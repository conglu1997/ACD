class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "A tree in autumn", "shape": "A tree with falling leaves"},
            "2": {"theme": "A winding river", "shape": "A winding path of a river"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a concrete poem based on the following theme and shape:

Theme: {t['theme']}
Shape: {t['shape']}

Your poem should visually represent the given shape and convey the theme through its language and arrangement. The visual arrangement of the text is crucial to the poem's meaning. Submit your poem as a plain text string.

Ensure your submission follows this format:
[Your concrete poem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should visually represent the given shape.", "The poem should convey the given theme through its language and arrangement.", "The poem should be coherent and meaningful."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

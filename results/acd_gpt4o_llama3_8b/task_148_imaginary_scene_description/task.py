class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "A futuristic cityscape at sunset"
            },
            "2": {
                "prompt": "An enchanted forest at midnight"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a vivid and detailed description of the following imaginary scene:

{t['prompt']}

Ensure that the description is coherent, engaging, and paints a clear picture of the scene in the reader's mind. The description should be between 150 to 300 words. Submit your description as a plain text string. Please adhere strictly to the word count."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should be vivid and detailed.",
            "The description should be coherent and engaging.",
            "The description should paint a clear picture of the scene in the reader's mind.",
            "The description should be between 150 to 300 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

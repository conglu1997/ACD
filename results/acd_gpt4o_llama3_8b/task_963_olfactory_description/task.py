class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"olfactory_cue": "The scent of freshly baked bread."},
            "2": {"olfactory_cue": "The smell of a pine forest after rain."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a detailed description based on the following olfactory cue: {t['olfactory_cue']}

Your description should be comprehensive and cover all aspects of the scent. Use vivid and precise language to ensure the scent can be easily imagined based on your description. The description should be at least 50 words long. Submit your response as a plain text string in the following format:

Description: [Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately represent the given olfactory cue.", "The description should be clear, vivid, and comprehensive.", "The description should be at least 50 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

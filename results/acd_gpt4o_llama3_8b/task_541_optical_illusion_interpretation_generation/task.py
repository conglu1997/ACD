class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"optical_illusion": "A black and white spiral that appears to move when you look at it.", "effect": "The illusion creates the effect of a moving spiral when viewed."},
            "2": {"concept": "A set of parallel lines that appear to bend or curve at certain points due to an overlay pattern.", "example": "The lines should appear straight but give the illusion that they are curving due to the background pattern."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'optical_illusion' in t:
            return f"""Interpret the visual effect of the given optical illusion. Describe what you see and explain the visual effect it creates. Submit your response as a plain text string in the following format:

Description: [Your description]
Effect: [The visual effect it creates]

Optical Illusion Description: {t['optical_illusion']}"""
        else:
            return f"""Generate a description for an optical illusion based on the given concept. Your description should be detailed and explain how the illusion works. Submit your response as a plain text string in the following format:

Description: [Your detailed description]
Effect: [The visual effect it creates]

Concept: {t['concept']}

Example: {t['example']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'optical_illusion' in t:
            criteria = [f"The response should accurately interpret the optical illusion effect as: {t['effect']}"]
        else:
            criteria = [f"The description should accurately convey the concept: {t['concept']}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

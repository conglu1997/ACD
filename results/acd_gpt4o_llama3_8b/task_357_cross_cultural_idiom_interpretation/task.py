class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "idiom": "Schwein haben",
                "culture": "German",
                "example": "In a challenging situation, if someone manages to succeed or escape trouble, a German might say they 'had a pig'."
            },
            "2": {
                "idiom": "猫をかぶる (neko wo kaburu)",
                "culture": "Japanese",
                "example": "In a social setting, if someone is pretending to be someone they're not to fit in, a Japanese person might say they are 'wearing a cat'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following idiom from {t['culture']} culture. Provide a detailed explanation of its meaning and give an example of how it would be used in context. Ensure your explanation is clear and culturally accurate.

Idiom: {t['idiom']}

Example of usage: {t['example']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The explanation should accurately convey the meaning of the idiom.", "The example of usage should be culturally appropriate and demonstrate correct usage of the idiom.", "The explanation should be clear and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

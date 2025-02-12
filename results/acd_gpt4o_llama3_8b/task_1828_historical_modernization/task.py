class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "narrative": "The story of King Arthur pulling the sword from the stone to become the rightful king of England."
            },
            "2": {
                "narrative": "The myth of Icarus flying too close to the sun with wings made of feathers and wax, leading to his fall."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reconstruct the following historical or mythological narrative in a modern setting:

Original Narrative: {t['narrative']}

Ensure that the modern version retains the core themes and lessons of the original story but adapts the characters, setting, and context to fit contemporary times. Your response should be a coherent and engaging narrative that clearly reflects the original plot and message in a modernized form. Submit your narrative as a plain text string in the following format:

Modernized Narrative: <your modernized narrative>"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The modernized narrative should retain the core themes and lessons of the original story.",
            "The modernized narrative should adapt the characters, setting, and context to fit contemporary times.",
            "The narrative should be coherent and engaging.",
            "The modernized version should clearly reflect the original plot and message."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

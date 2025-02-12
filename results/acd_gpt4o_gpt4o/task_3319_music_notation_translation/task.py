class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "G4 A4 B4 C5 D5 E5 F#5 G5", "type": "translate"},
            "2": {"description": "A sequence of ascending notes starting from G4 to G5, with the F note being sharp.", "type": "generate"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "translate":
            return f"""Your task is to translate the following musical notation into descriptive text: {t["notation"]}. Ensure your description clearly conveys the sequence of notes, including any sharps, flats, or special instructions. Provide your description in a coherent and clear narrative format. Your response should be in the form 'Description: [Your description]'."""
        else:
            return f"""Your task is to generate musical notation based on the following description: '{t["description"]}'. Ensure your notation accurately represents the described sequence of notes, including any sharps, flats, or special instructions. Provide your response in standard musical notation format. Your response should be in the form 'Notation: [Your notation]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "translate":
            criteria = ["The description should clearly and accurately convey the sequence of notes, including any sharps or flats."]
        else:
            criteria = ["The musical notation should accurately represent the described sequence of notes, including any sharps or flats."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

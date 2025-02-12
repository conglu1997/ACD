class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "4/4 time signature, 8 measures, use the notes C, D, E, F, G, A, B"
            },
            "2": {
                "notation": "C4 E4 G4 F4 | E4 D4 C4 G4 | A4 B4 C5 D5 | E4 F4 G4 A4 | B4 C5 D5 E5 | F4 G4 A4 B4 | C5 B4 A4 G4 | F4 E4 D4 C4"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'constraints' in t:
            return f"""Generate a simple melody based on the following constraints: {t['constraints']}. Submit your melody as a plain text string in the following format: 'Melody: [Your melody in standard music notation]'. Ensure the melody follows the given constraints and is musically coherent."""
        elif 'notation' in t:
            return f"""Interpret the following music notation into a textual description of the melody. Notation: {t['notation']}. Submit your description as a plain text string in the following format: 'Description: [Your description]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'constraints' in t:
            validation_criteria = [
                "The melody should be in 4/4 time signature.",
                "The melody should consist of 8 measures.",
                "The melody should use the notes C, D, E, F, G, A, B.",
                "The melody should be musically coherent."
            ]
        elif 'notation' in t:
            validation_criteria = [
                "The description should accurately represent the given music notation.",
                "The description should be clear and understandable."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

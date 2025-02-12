class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 E4 G4 C5",
                "criteria": "Create a four-note melody in the key of C major that starts with the note G4. The melody should be musically coherent."
            },
            "2": {
                "notation": "G3 B3 D4 G4",
                "criteria": "Create a four-note melody in the key of G major that ends with the note D4. The melody should be musically coherent."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task 1: Interpret the following musical notation: {t['notation']}.
Describe the notes and their sequence. Be specific about the pitch and order of the notes.

Task 2: {t['criteria']}
Generate a four-note melody based on the criteria. Ensure the melody is musically coherent and follows the key and starting/ending note requirements.

Submit your responses in the following format:

1. Interpretation:
[Your interpretation of the given notation]

2. Melody:
[Your generated melody based on the criteria]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should accurately describe the pitch and order of the notes.",
            "The generated melody should be musically coherent and adhere to the given criteria, including the key and starting/ending note."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Generate a 4-bar melody in C major using standard musical notation."
            },
            "2": {
                "melody": "C4 E4 G4 C5 | D4 F4 A4 D5 | E4 G4 B4 E5 | F4 A4 C5 F5"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'criteria' in t:
            return f"""Generate a short piece of music based on the following criteria. Provide the music in standard musical notation format (e.g., using letters and numbers to represent notes and octaves).\n\nCriteria: {t['criteria']}\n\nExample response format:\nC4 E4 G4 C5 | D4 F4 A4 D5 | E4 G4 B4 E5 | F4 A4 C5 F5"""
        elif 'melody' in t:
            return f"""Transcribe the following piece of music into standard musical notation. Provide your transcription in a clear format.\n\nMelody: {t['melody']}\n\nExample response format:\nC4 E4 G4 C5 | D4 F4 A4 D5 | E4 G4 B4 E5 | F4 A4 C5 F5"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'criteria' in t:
            validation_criteria = [
                "The generated music should be coherent and follow the given criteria.",
                "The music should be presented in standard musical notation."
            ]
        else:
            validation_criteria = [
                "The transcription should accurately represent the given melody.",
                "The transcription should be presented in a clear format."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

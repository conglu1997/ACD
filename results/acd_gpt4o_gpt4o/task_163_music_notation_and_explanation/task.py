class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Write a simple melody in C major, 4/4 time signature, using whole, half, quarter and eighth notes. The melody should be 8 bars long and contain at least 16 notes."},
            "2": {"notation": "C4, D4, E4, F4, G4, A4, B4, C5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'description' in t:
            return f"""Your task is to generate musical notation based on the following description:

Description: {t['description']}

Ensure your notation follows the musical theory principles described in the prompt. Provide your notation in plain text format using the format 'NoteOctave, NoteOctave, ...' (e.g., 'C4, D4, E4, F4, G4, A4, B4, C5')."""
        else:
            return f"""Your task is to explain the following musical notation in terms of note names, their octave, and their position in the C major scale:

Notation: {t['notation']}

Example explanation format: 
- C4: C note in the 4th octave, 1st note in the C major scale.
- D4: D note in the 4th octave, 2nd note in the C major scale.
Ensure your explanation includes the note names, their octave, and their position in the scale. Provide your explanation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'description' in t:
            criteria = ["The notation should follow the musical theory principles described in the prompt.", "The notation should be in the correct format 'NoteOctave, NoteOctave, ...'.", "The melody should be 8 bars long.", "The melody should contain at least 16 notes."]
        else:
            criteria = ["The explanation should correctly identify the note names, their octave, and their position in the C major scale."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

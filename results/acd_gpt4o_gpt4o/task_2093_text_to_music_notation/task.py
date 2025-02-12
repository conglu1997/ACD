class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A simple melody in C major starting with C, followed by E, G, C (octave higher), B, G, E, and ending with C."},
            "2": {"description": "A short tune in G major starting with G, followed by B, D, G (octave higher), F#, D, B, and ending with G."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to convert the following textual description of a musical piece into a simplified musical notation:

Description: {t['description']}

The notation should use standard musical notes (C, D, E, F, G, A, B) and indicate any sharps or flats where necessary. Provide the notation in plain text format, separating each note with a comma.

Format: Note1, Note2, Note3, ...

Example:

Description: A simple melody in C major starting with C, followed by D, E, F, G, A, B, and ending with C.
Notation: C, D, E, F, G, A, B, C."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The notation should correctly represent the sequence of notes described in the text.",
            "Any sharps or flats should be accurately indicated.",
            "The notation should be clear and correctly formatted with notes separated by commas."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {'text_description': 'A melody starting with a G4 quarter note, followed by an A4 half note, a B4 eighth note, a C5 quarter note, and ending with a D5 whole note.'},
            '2': {'musical_notation': 'E4 (quarter), F4 (eighth), F4 (eighth), G4 (quarter), A4 (half), B4 (whole)'}
        }
        assert len(tasks) == 2, 'There should be exactly two tasks.'
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'text_description' in t:
            return f"""Convert the following textual description of a melody into musical notation.

Text Description: {t['text_description']}

Provide the musical notation in the following format: [Note] ([Duration]). Separate each note by a comma.
Example: C4 (whole), E4 (half), F4 (quarter)
"""
        elif 'musical_notation' in t:
            return f"""Generate a textual description from the following musical notation.

Musical Notation: {t['musical_notation']}

Provide the description in plain text format, detailing the sequence of notes and their durations.
Example: A melody consisting of an E4 whole note, followed by an F4 half note, and ending with a G4 quarter note.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

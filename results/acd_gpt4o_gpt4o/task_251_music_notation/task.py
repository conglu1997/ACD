class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"melody": "C D E F G A B C", "octaves": [4, 4, 4, 4, 4, 4, 4, 5]},
            "2": {"notation": "C4 D4 E4 F4 G4 A4 B4 C5"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "melody" in t:
            octaves = t["octaves"]
            return f"""Convert the following melody into musical notation with the given octaves: {t['melody']}.

Use the following format for musical notation:
- Each note should be followed by its octave number (e.g., C4, D4).
- Separate each note with a space.

Submit your answer in plain text format."""
        elif "notation" in t:
            return f"""Generate a melody based on the following musical notation: {t['notation']}.

Ensure the melody is coherent and follows the given notation accurately.

Submit your answer in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []

        if "melody" in t:
            melody_notes = t['melody'].split()
            octaves = t['octaves']
            expected = " ".join([f"{note}{octave}" for note, octave in zip(melody_notes, octaves)])
            criteria.append(f"The response should match the expected notation: {expected}.")
        elif "notation" in t:
            notation_notes = t['notation'].split()
            expected = " ".join([note[:-1] for note in notation_notes])
            criteria.append(f"The response should match the expected melody: {expected}.")

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
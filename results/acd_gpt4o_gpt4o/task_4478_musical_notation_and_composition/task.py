class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "4/4 c4 d8 f g16 a g f#"},
            "2": {"theme": "happy", "key": "C Major", "length": "4 measures"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "notation" in t:
            return f"""Your task is to interpret the following piece of musical notation and describe it in plain text:

Notation: {t['notation']}

Provide a detailed description of the melody, including the notes, rhythm, and any other relevant musical elements. Include the following details:

1. The time signature.
2. The sequence of notes.
3. The rhythm of each note (e.g., quarter note, eighth note).
4. Any notable patterns or repetitions.
5. The overall mood or feel of the melody."""
        else:
            return f"""Your task is to generate a short musical composition based on the following theme:

Theme: {t['theme']}
Key: {t['key']}
Length: {t['length']}

Provide the composition in the form of simple musical notation. Ensure that the composition is coherent and fits the given theme. Include the following elements:

1. A clear melody line.
2. Appropriate rhythm for each note.
3. Consistency with the specified key.
4. A sense of progression or development over the measures.
5. An overall mood that matches the theme."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "notation" in t:
            criteria = ["The description should accurately describe the time signature.", "The description should list the sequence of notes correctly.", "The description should include the rhythm of each note.", "The description should mention any notable patterns or repetitions.", "The description should convey the overall mood or feel of the melody."]
        else:
            criteria = ["The composition should include a clear melody line.", "The composition should use appropriate rhythm for each note.", "The composition should be consistent with the specified key.", "The composition should show a sense of progression or development.", "The composition should match the overall mood of the theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

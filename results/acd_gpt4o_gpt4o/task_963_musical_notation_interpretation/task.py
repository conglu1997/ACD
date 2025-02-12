class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "4/4 | C4 D4 E4 F4 | G4 A4 B4 C5 | mf"},
            "2": {"notation": "3/4 | G4 G4 G4 | E4 E4 E4 | D4 D4 D4 | p"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        notation = t["notation"]
        instructions = f"""Your task is to interpret the following musical notation and provide a detailed description of the music represented by it:

Notation: {notation}

Your description should include:
1. The time signature and its meaning.
2. The sequence of notes and their respective durations.
3. Any patterns or repetitions in the melody.
4. Dynamics and other musical expressions (e.g., forte, piano) if present.

Ensure your description is clear and detailed, suitable for someone with a basic understanding of musical notation. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should correctly interpret the time signature.", "The sequence of notes and their durations should be accurately described.", "Any patterns or repetitions in the melody should be identified.", "Dynamics and other musical expressions should be mentioned if present."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

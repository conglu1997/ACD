class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A simple melody with three notes: C4 quarter note, D4 quarter note, E4 half note."},
            "2": {"description": "A simple rhythm pattern: quarter rest, quarter note C4, half note D4."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate musical notation based on the following description:

{t['description']}

1. Use standard musical notation symbols.
2. Provide the musical notation in a plain text format where 'C4' represents the note C in the fourth octave, 'quarter note' is represented as 'q', 'half note' as 'h', 'quarter rest' as 'R', and so on.
3. Ensure that the notation is accurate and corresponds to the given description.

For example, for the description 'A simple melody with two notes: C4 quarter note, D4 half note', the notation would be:
C4 q, D4 h
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The musical notation should accurately represent the given description.",
            "The notation should use standard musical symbols and follow the described format.",
            "The sequence and duration of notes and rests should match the description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

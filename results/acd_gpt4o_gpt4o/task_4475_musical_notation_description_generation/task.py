class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "C4 E4 G4 C5 E5", "description": "A simple C major arpeggio played in an ascending order."},
            "2": {"notation": "G4 B4 D5 F#5 G5", "description": "A G major 7th chord played in a broken manner, followed by the root note again."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        notation = t["notation"]
        description = t["description"]
        instructions = f"""Your task involves two parts:\n\n1. Interpretation: Interpret the given piece of musical notation and describe its musical elements.\n\nNotation: {notation}\n\nYour interpretation should include details such as the notes used, any chords formed, the sequence and intervals of the notes, and the overall musical idea conveyed.\n\n2. Generation: Create a new piece of musical notation based on the provided description.\n\nDescription: {description}\n\nYour generated notation should be coherent and accurately reflect the given description.\n\nResponse Format:\nInterpretation: <Your interpretation>\nGenerated Notation: <Your notation>\n\nProvide both parts in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should include details such as the notes used, any chords formed, the sequence and intervals of the notes, and the overall musical idea conveyed.",
            "The generated notation should be coherent and accurately reflect the given description."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 E4 G4 C5",
                "parameters": "Compose a short piece of music in C major, using the given notes as the starting motif. Ensure the piece is 8 measures long, includes a variety of note durations, and uses dynamics (e.g., forte, piano)."
            },
            "2": {
                "notation": "A3 C4 E4 A4",
                "parameters": "Compose a short piece of music in A minor, using the given notes as the starting motif. Ensure the piece is 8 measures long, includes a variety of note durations, and uses dynamics (e.g., forte, piano)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Interpret the following musical notation: {t['notation']}. {t['parameters']} Provide your response in plain text, using standard musical notation (e.g., C4, D4, E4) to indicate the notes and their respective durations (e.g., quarter notes, eighth notes) and dynamics (e.g., forte, piano)."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly interpret the given notation.",
            "The composition should adhere to the given parameters (key, length, variety of note durations, and dynamics).",
            "The composition should be musically coherent and maintain the given motif."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

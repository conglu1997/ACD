class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"musical_score": "C4 E4 G4 | D4 F#4 A4 | E4 G4 B4 | F4 A4 C5 | G4 B4 D5"},
            "2": {"description": "Generate a musical score where each measure consists of a sequence of ascending notes starting from C4 to G4, with each measure containing three notes."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "musical_score" in t:
            return f"""Your task is to interpret the following musical score and describe it in plain text:

{t["musical_score"]}

Provide a detailed description of the musical score, including the notes in each measure and any identifiable patterns or chords. Indicate any sharps or flats explicitly. Describe each measure separately."""
        elif "description" in t:
            return f"""Your task is to generate a musical score based on the following description:

{t["description"]}

Ensure that the musical score is accurate and adheres to the given description. Provide the musical score in a standard format, with each measure separated by a vertical bar (|). Each measure should contain exactly three notes in an ascending sequence from C4 to G4."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "musical_score" in t:
            criteria = [
                "The response should describe the notes in each measure.",
                "The response should identify any patterns or chords.",
                "The response should indicate any sharps or flats explicitly.",
                "The response should describe each measure separately.",
            ]
        elif "description" in t:
            criteria = [
                "The generated musical score should match the given description.",
                "Each measure should be separated by a vertical bar (|).",
                "Each measure should contain the correct sequence of notes as described.",
                "Each measure should contain exactly three notes in an ascending sequence from C4 to G4.",
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

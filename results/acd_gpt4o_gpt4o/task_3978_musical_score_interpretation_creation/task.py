class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"score": "C4 E4 G4 C5 D5 F5 A5"},
            "2": {"theme": "A calm and serene melody in the key of F major, using at least 8 different notes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "score" in t:
            return f"""Your task is to interpret the following musical score and describe it in detail:

Score: {t["score"]}

Provide a detailed description of the musical score, including the key, the notes, the rhythm, and any other relevant musical elements. Your description should be clear and accurate, reflecting a deep understanding of music theory. Provide your response in plain text format."""
        elif "theme" in t:
            return f"""Your task is to create a new musical piece based on the following theme:

Theme: {t["theme"]}

Compose a short musical piece that fits the given theme. Provide the musical notation in a text format (e.g., C4 E4 G4 C5 for notes). Ensure that your composition is coherent, matches the specified criteria, and uses at least 8 different notes. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "score" in t:
            criteria = ["The description should accurately reflect the notes in the score.", "The description should include key musical elements like key, rhythm, and structure."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
        elif "theme" in t:
            criteria = ["The composition should fit the given theme.", "The notation should be clear and accurate.", "The piece should be coherent and musically valid.", "The composition should use at least 8 different notes."]
            return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

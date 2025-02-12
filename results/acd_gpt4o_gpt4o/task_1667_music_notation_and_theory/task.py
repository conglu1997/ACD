class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "Interpret Musical Notation",
                "notation": "C4 E4 G4 C5 | D4 F#4 A4 D5 | E4 G#4 B4 E5"
            },
            "2": {
                "title": "Generate Musical Piece",
                "theme": "A happy birthday tune",
                "constraints": "Include the notes C, G, and E in the melody. Use at least 8 measures. Incorporate at least 2 different time signatures and include dynamics (e.g., forte, piano)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['title'] == "Interpret Musical Notation":
            instructions = f"""Your task is to interpret the given musical notation and provide a description of the melody.\n\nNotation: {t['notation']}\n\nYour description should include:\n1. The key of the melody.\n2. The sequence of notes in plain text (e.g., C4, E4, G4, C5).\n3. Any notable musical characteristics (e.g., intervals, rhythm, time signatures).\n4. Explicitly identify the time signatures used.\n\nProvide your response in plain text format."""
        elif t['title'] == "Generate Musical Piece":
            instructions = f"""Your task is to generate a new musical piece based on the provided theme and constraints.\n\nTheme: {t['theme']}\nConstraints: {t['constraints']}\n\nYour musical piece should be original and adhere to the given constraints. Provide your response in plain text format, including the musical notation in standard notation format, specifying the tempo, and a brief description of the piece."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['title'] == "Interpret Musical Notation":
            criteria = [
                "The response should correctly identify the key of the melody.",
                "The response should list the notes in the correct sequence.",
                "The response should describe any notable musical characteristics, including intervals, rhythm, and time signatures.",
                "The response should explicitly identify the time signatures used."
            ]
        elif t['title'] == "Generate Musical Piece":
            criteria = [
                "The musical piece should be original.",
                "The piece should include the notes C, G, and E in the melody.",
                "The piece should have at least 8 measures.",
                "The piece should incorporate at least 2 different time signatures.",
                "The piece should include dynamics (e.g., forte, piano).",
                "The piece should specify the tempo.",
                "The piece should adhere to the happy birthday theme."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

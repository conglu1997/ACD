class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "G4 E4 F4 G4 | A4 G4 F4 E4 | D4 D4 D4 D4 | E4 F4 G4 A4"},
            "2": {"description": "A simple melody with the notes G, E, F, and G in the first bar, followed by A, G, F, and E in the second bar, then four D notes in the third bar, and ending with E, F, G, and A in the last bar."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "notation" in t:
            return f"""You are given a piece of music notation. Your task is to provide a textual description of the melody and rhythm. Describe the sequence of notes and the structure of the bars clearly.

Music Notation: {t['notation']}

Response Format:
Description: [Provide a detailed description of the melody and rhythm, including the sequence of notes and bar structure.]"""
        elif "description" in t:
            return f"""You are given a textual description of a melody and rhythm. Your task is to generate the corresponding music notation. Ensure that the notation accurately reflects the melody and rhythm described.

Description: {t['description']}

Response Format:
Notation: [Provide the music notation that corresponds to the described melody and rhythm.]"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "notation" in t:
            criteria = ["The response should clearly describe the sequence of notes and the structure of the bars as given in the notation.", "The description should be accurate and comprehensive."]
        elif "description" in t:
            criteria = ["The generated notation should accurately reflect the melody and rhythm described.", "The notation should be formatted correctly."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

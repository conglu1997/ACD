class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "musical_piece": "C4-E4-G4-C5\nE4-G4-B4-E5\nG4-B4-D5-G5\nC4-E4-G4-C5\nA4-C5-E5-A5\nF4-A4-C5-F5",
                "instructions": "1. Analyze the given musical piece and identify the chords being played.\n2. Generate a new musical piece of similar length that follows a different chord progression while maintaining the same rhythm and tempo.\n3. Return both the identified chords and the new musical piece."
            },
            "2": {
                "musical_piece": "A3-C4-E4-A4\nD4-F4-A4-D5\nF4-A4-C5-F5\nA3-C4-E4-A4\nG3-B3-D4-G4\nE3-G3-B3-E4",
                "instructions": "1. Analyze the given musical piece and identify the key and scale being used.\n2. Generate a new musical piece of similar length that modulates to a different key while maintaining the same rhythm and tempo.\n3. Return both the identified key and scale, and the new musical piece."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and generate musical compositions based on the given criteria:\n{t['instructions']}\n\nMusical Piece:\n{t['musical_piece']}\n\nSubmit your response as a plain text string in the following format:\nIdentified Chords/Key and Scale: [Your analysis]\nNew Musical Piece: [Your new musical piece]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        response_format_criteria = [
            "The response should start with 'Identified Chords/Key and Scale:' followed by the analysis.",
            "The response should include 'New Musical Piece:' followed by the new musical piece.",
            "The identified chords/key and scale should be consistent with the given musical piece.",
            "The new musical piece should follow the specified criteria of chord progression or modulation while maintaining the same rhythm and tempo."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, response_format_criteria) else 0.0

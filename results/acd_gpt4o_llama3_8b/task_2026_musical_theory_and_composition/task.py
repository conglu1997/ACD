class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Compose a 16-bar melody in 4/4 time signature, using the C major scale. Include at least one modulation to a different key (e.g., G major or A minor) and indicate the modulation point." 
            },
            "2": {
                "music_piece": "G-G-G-E, G-G-G-D, G-G-G-E, G-G-G-D, E-E-E-D, E-E-E-C, E-E-E-D, E-E-E-C, F-F-F-F, F-F-F-E, F-F-F-F, F-F-F-E, G-G-G-G, G-G-G-E, G-G-G-G, G-G-G-E" 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            return f"""Compose a 16-bar melody in 4/4 time signature, using the C major scale. Ensure that your composition includes at least one modulation to a different key (e.g., G major or A minor) and indicate the modulation point. Submit your composition as a plain text string in the following format: \nBar 1: [notes, e.g., C4 E4 G4 C5] \nBar 2: [notes, e.g., D4 F4 A4 D5] \n... \nBar 16: [notes]."""
        elif "music_piece" in t:
            return f"""Analyze the following piece of music. Provide a detailed analysis of the melody, harmony, and rhythm. Include an explanation of any notable musical features and the overall structure of the piece. Submit your analysis as a plain text string in the following format: \nMelody: ... \nHarmony: ... \nRhythm: ... \nStructure: ... \n\nMusic Piece: {t['music_piece']}"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            validation_criteria = [
                "The composition should be 16 bars long.",
                "The composition should use the C major scale.",
                "The composition should include at least one modulation to a different key (e.g., G major or A minor).",
                "The modulation point should be clearly indicated."
            ]
        else:
            validation_criteria = [
                "The analysis should cover melody, harmony, rhythm, and structure.",
                "The analysis should be detailed and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 E4 G4 C5 E5 G5 C6 E6 G6",
                "style": "classical",
                "structure": "ABA"
            },
            "2": {
                "notation": "D4 F#4 A4 C5 E5 G5 B5 D6 F#6",
                "style": "jazz",
                "structure": "AAB"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following musical notation and create a new composition with the specified style and structure.

Notation: {t['notation']}

Style: {t['style']}
Structure: {t['structure']}

Your response should include:
1. An interpretation of the given musical notation, explaining its melody, harmonic progressions, and any notable patterns.
2. A new musical composition that adheres to the specified style and structure. For example, if the structure is ABA, ensure the composition follows the pattern where the first and third sections are similar, and the second section contrasts.

Example:
Interpretation: The given notation starts with a simple triad and builds up to a higher octave, creating a sense of progression and climax.
New Composition: C4 E4 G4 C5 E5 G5 C6 E6 G6 | A4 C5 E5 G5 B5 D6 | C4 E4 G4 C5 E5 G5 C6 E6 G6

Submit your response as a plain text string in the following format:
Interpretation: [Your interpretation]
New Composition: [Your new composition]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The interpretation should accurately describe the melody, harmonic progressions, and any notable patterns in the given notation.",
            "The new composition should adhere to the specified style and structure, including the correct pattern (e.g., ABA or AAB) and stylistic elements (e.g., classical or jazz)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

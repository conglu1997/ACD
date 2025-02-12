class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Compose a short piece of music (8-16 bars) that conveys a sense of mystery. Use a minor key and include at least one modulation."
            },
            "2": {
                "theme": "Compose a short piece of music (8-16 bars) that conveys a sense of joy. Use a major key and include a repeating motif."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short piece of music based on the given theme. Your composition should be between 8 to 16 bars long and must adhere to the specified instructions.

Theme: {t['theme']}

Your response should include:
1. A description of the composition, explaining how it adheres to the theme and the specified musical elements.
2. The musical notation for the composition, using standard musical notation symbols.

Example response format:
- Description: The piece is in a minor key and conveys a sense of mystery through the use of dissonant harmonies and unexpected modulations. It includes a modulation from A minor to C minor in the fifth bar, enhancing the sense of mystery.
- Musical Notation: A minor: | A4 C4 E4 A4 | G4 B4 D5 G5 | F#4 A4 C5 F#5 | E4 G4 B4 E5 | Modulation to C minor: | C4 E4 G4 C5 | D4 F4 A4 D5

Submit your response as a plain text string in the following format:
- Description: [Your description here]
- Musical Notation: [Your musical notation here]

Ensure your description is clear and precise, and the musical notation is accurate and follows standard conventions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The description should accurately capture how the composition adheres to the theme and specified musical elements.",
            "The musical notation should be accurate and follow standard conventions.",
            "The composition should be coherent and musically valid.",
            "The composition should be between 8 to 16 bars long.",
            "The composition should include the specified musical elements (e.g., minor key, modulation, major key, repeating motif)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

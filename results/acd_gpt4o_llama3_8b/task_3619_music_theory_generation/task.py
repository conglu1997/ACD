class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "generate_scale",
                "notes": "C, D, E, F, G, A, B"
            },
            "2": {
                "type": "identify_chord_progression",
                "chords": "C, G, Am, F, Dm"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'generate_scale':
            return f"""Generate a musical scale based on the following notes:

Notes: {t['notes']}

Ensure the scale is logically consistent, follows standard music theory conventions, and includes any necessary accidentals (sharps or flats). Your response should indicate the type of scale (e.g., major, minor, pentatonic) and follow standard notation. Submit your response as a plain text string in the format: [Musical Scale]. Example: 'C, D, E, F, G, A, B'."""
        else:
            return f"""Identify the chord progression based on the following chords:

Chords: {t['chords']}

Ensure your identification is accurate, and explain the progression in terms of music theory, including Roman numeral analysis. Your response should also include a brief explanation of the harmonic function of each chord within the progression. Submit your response as a plain text string in the format: [Chord Progression: Explanation]. Example: 'I-V-vi-IV: This is a common chord progression in popular music, where I is the tonic, V is the dominant, vi is the submediant, and IV is the subdominant.'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'generate_scale':
            validation_criteria = ["The response should be a logically consistent musical scale based on the provided notes, include necessary accidentals, and follow standard music theory conventions."]
        else:
            validation_criteria = ["The response should accurately identify the chord progression, include Roman numeral analysis, and explain the harmonic function of each chord."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

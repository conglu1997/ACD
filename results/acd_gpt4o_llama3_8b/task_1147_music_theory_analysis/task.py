class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "piece": "Twinkle Twinkle Little Star",
                "requirements": "Analyze the melody, harmony, and structure of the piece. Discuss the key, scale, chord progression, and any notable musical elements. Provide specific examples from the piece to support your analysis."
            },
            "2": {
                "piece": "Beethoven's Symphony No. 5, First Movement",
                "requirements": "Analyze the first movement of Beethoven's Symphony No. 5. Discuss the key, motifs, dynamics, and the overall structure of the movement. Highlight any significant musical techniques used by Beethoven. Provide specific examples from the piece to support your analysis."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and describe the following musical piece based on the given music theory concepts:

Piece: {t['piece']}

Requirements: {t['requirements']}

Your response should include a thorough analysis of the melody, harmony, structure, key, scale, chord progression, and any notable musical elements. Provide specific examples from the piece to support your analysis. Submit your analysis as a plain text string with the following sections:

1. Melody: [Your analysis of the melody]
2. Harmony: [Your analysis of the harmony]
3. Structure: [Your analysis of the structure]
4. Key and Scale: [Your analysis of the key and scale]
5. Chord Progression: [Your analysis of the chord progression]
6. Notable Elements: [Your analysis of any notable musical elements]
7. Examples: [Specific examples from the piece supporting your analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should cover all specified sections.",
            "The descriptions should be coherent and relevant to the piece.",
            "The musical elements should be accurately identified and described.",
            "Specific examples from the piece should be provided to support the analysis."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

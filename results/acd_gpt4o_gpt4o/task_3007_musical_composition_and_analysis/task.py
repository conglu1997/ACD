class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"analysis_piece": "Twinkle Twinkle Little Star", "composition_instructions": "Compose a new piece in the style of a lullaby."},
            "2": {"analysis_piece": "Beethoven's Symphony No. 5", "composition_instructions": "Compose a new piece in the style of classical symphony."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: analysis and composition.

Part 1: Analysis
Analyze the given musical piece, considering its structure, melody, harmony, rhythm, and overall style.

Musical Piece: {t['analysis_piece']}

Provide your analysis in the following format:
Analysis:
- Structure: [Describe the structure of the piece]
- Melody: [Describe the melody of the piece]
- Harmony: [Describe the harmony of the piece]
- Rhythm: [Describe the rhythm of the piece]
- Style: [Describe the overall style of the piece]

Part 2: Composition
Compose a new musical piece based on the given instructions. Ensure your composition aligns with the specified style and demonstrates creativity and coherence.

Composition Instructions: {t['composition_instructions']}

Provide your composition in the following format:
Composition:
- Title: [Title of your composition]
- Melody: [Describe the melody of your composition]
- Harmony: [Describe the harmony of your composition]
- Rhythm: [Describe the rhythm of your composition]
- Style: [Describe the overall style of your composition]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately describe the structure, melody, harmony, rhythm, and style of the piece.",
            "The composition should align with the specified style and demonstrate creativity and coherence.",
            "The submission should cover both parts: analysis and composition.",
            "The response should follow the specified format." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

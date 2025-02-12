class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "criteria": "Compose a short piece of music (8 measures) in the style of a waltz (3/4 time signature). Use at least one chord progression and ensure the piece is harmonically coherent."
            },
            "2": {
                "criteria": "Analyze the following musical composition and identify any recurring motifs or patterns. Explain how these motifs contribute to the overall structure and feel of the piece. Composition: C-E-G, E-G-B, G-B-D, B-D-F#, E-G-B, G-B-D, B-D-F#, C-E-G (repeats)."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to complete the following music-related task based on the given criteria.

Criteria: {t['criteria']}

For Task 1, provide your musical composition in plain text format, using standard musical notation (e.g., C-E-G for a C major chord). Ensure your composition is 8 measures long and follows the waltz style in 3/4 time signature.

For Task 2, provide your analysis in plain text format. Identify any recurring motifs or patterns in the given composition and explain their contribution to the overall structure and feel of the piece. Your explanation should be detailed and logically structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'Compose' in t['criteria']:
            criteria = [
                "The composition should be 8 measures long.",
                "The piece should be in the style of a waltz (3/4 time signature).",
                "The composition should include at least one chord progression.",
                "The composition should be harmonically coherent."
            ]
        else:
            criteria = [
                "The analysis should correctly identify recurring motifs or patterns.",
                "The explanation should be detailed and logical.",
                "The analysis should explain how the motifs contribute to the overall structure and feel of the piece."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

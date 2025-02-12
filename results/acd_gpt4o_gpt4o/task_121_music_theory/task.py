class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scale": "C Major"},
            "2": {"chord_progression": "I-IV-V-I in G Major"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'scale' in t:
            return f"""Your task is to identify the notes in the following musical scale:

Scale: {t['scale']}

Provide the notes in the scale in ascending order, separated by commas. Example format: 'C, D, E, F, G, A, B'"""
        else:
            return f"""Your task is to generate a chord progression based on the given instructions:

Chord Progression: {t['chord_progression']}

Provide the chord names in the progression in the correct order, separated by commas. Example format: 'G, C, D, G'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'scale' in t:
            criteria = ["The notes should be listed in ascending order, separated by commas.", "The notes must be correct for the given scale."]
        else:
            criteria = ["The chords should be listed in the correct order, separated by commas.", "The chords must be correct for the given chord progression."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

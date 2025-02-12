class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C major", "progression": "I-IV-V-I"},
            "2": {"key": "G major", "progression": "I-vi-IV-V"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate and analyze a chord progression based on the given key and progression formula. Provide the chords in the progression and a brief explanation of the musical qualities and emotional effects of the progression.

Key: {t['key']}
Progression: {t['progression']}

Your response should be in the following format:
Chords: [List of chords]
Analysis: [Your explanation of the musical qualities and emotional effects]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The submission should correctly generate the chords according to the given key and progression.", "The explanation should describe the musical qualities and emotional effects accurately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

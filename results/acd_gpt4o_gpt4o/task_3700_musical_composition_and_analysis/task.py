class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"criteria": "Compose a 4-bar melody in C major using only quarter notes."},
            "2": {"piece": "C-D-E-F-G-A-B-C", "analysis": "Identify the scale and key of the provided melody and describe its structure, including any patterns or repetitions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'criteria' in t:
            return f"""Your task is to compose a short piece of music based on the given criteria.

Criteria: {t['criteria']}

Your response should include the melody in plain text format, using letters to represent notes (e.g., C-D-E-F). Provide your composition in plain text without any additional formatting."""
        else:
            return f"""Your task is to analyze the provided piece of music and describe its key and structure, including any patterns or repetitions.

Piece: {t['piece']}
Analysis: {t['analysis']}

Your response should include the identified scale and key, and a brief description of the musical structure in plain text format without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'criteria' in t:
            criteria = [
                "The composition should be a 4-bar melody.",
                "The melody should be in C major.",
                "Only quarter notes should be used."
            ]
        else:
            criteria = [
                "The identified scale and key should be correct.",
                "The description of the musical structure should be accurate.",
                "The analysis should identify any patterns or repetitions in the melody."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

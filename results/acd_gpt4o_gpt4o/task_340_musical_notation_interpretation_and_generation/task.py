class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "C4 E4 G4 C5 E5 G5"},
            "2": {"notation": "D4 F#4 A4 D5 F#5 A5"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following piece of musical notation and generate a new piece based on the given transformation instructions:

{t["notation"]}

Transformation Instructions:
1. Transpose the notation up by one whole step. For example, 'C4' becomes 'D4', 'E4' becomes 'F#4', etc.
2. Change the rhythm to a syncopated pattern. For example, if the original rhythm was [1, 2, 3, 4], a syncopated rhythm might be [1, 1.5, 2.5, 3].
3. Add a rest after every fourth note. For example, if the original sequence was 'C4 E4 G4 C5 E5 G5', the new sequence might be 'D4 F#4 A4 D5 (rest) F#5 A5'.

Provide your new piece of musical notation in the following format:

Original Notation: {t["notation"]}
New Notation: [new notation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new notation should be correctly transposed up by one whole step.",
            "The rhythm should be changed to a syncopated pattern.",
            "There should be a rest after every fourth note.",
            "The submission should maintain the same format as the original notation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

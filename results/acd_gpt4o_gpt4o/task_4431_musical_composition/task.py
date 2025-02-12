class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": {
                    "key": "C Major",
                    "time_signature": "4/4",
                    "length_in_bars": 4,
                    "required_intervals": ["major third", "perfect fifth"]
                },
                "task": "Create a melody based on the given constraints."
            },
            "2": {
                "melody": "C4 E4 G4 E4 | F4 A4 C5 A4 | G4 B4 D5 B4 | C5 E5 G5 E5",
                "task": "Interpret the emotional tone of the given melody."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            constraints = t["constraints"]
            key = constraints["key"]
            time_signature = constraints["time_signature"]
            length_in_bars = constraints["length_in_bars"]
            required_intervals = ', '.join(constraints["required_intervals"])
            instructions = f"""Your task is to create a melody based on the following constraints:

Key: {key}
Time Signature: {time_signature}
Length: {length_in_bars} bars
Required Intervals: {required_intervals}

Provide your melody in a format similar to the following example:
C4 E4 G4 E4 | F4 A4 C5 A4 | G4 B4 D5 B4 | C5 E5 G5 E5

Your melody should be original, follow the given constraints strictly, and be musically coherent.
"""
        else:
            melody = t["melody"]
            instructions = f"""Your task is to interpret the emotional tone of the following melody:

Melody: {melody}

Provide your interpretation in plain text format, explaining the emotional tone of the melody and identifying the musical elements that contribute to this tone.
Your interpretation should be detailed, reflecting an understanding of how melody and musical elements convey emotion.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = [
                "The melody should be in the key of C Major.",
                "The melody should follow a 4/4 time signature.",
                "The melody should be 4 bars long.",
                "The melody should include the required intervals.",
                "The melody should be presented in a format similar to the example.",
                "The melody should be original and musically coherent."
            ]
        else:
            criteria = [
                "The interpretation should accurately reflect the emotional tone of the melody.",
                "The interpretation should identify the musical elements contributing to the tone.",
                "The interpretation should be detailed and reflect an understanding of musical theory."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

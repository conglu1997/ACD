class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "C major, 4 bars, 4/4 time signature, note range C4 to G5, quarter notes only"},
            "2": {"music_piece": "Twinkle, Twinkle, Little Star"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            constraints = t['constraints']
            return f"Generate a simple melody based on the following constraints: {constraints}. Ensure the melody is coherent, follows the given constraints, and is musically pleasing. Submit your melody as a sequence of notes in the following format: 'C4, E4, G4, C5, ...'."
        else:
            music_piece = t['music_piece']
            return f"Analyze the following piece of music: {music_piece}. Identify the key features of the piece, including its key, time signature, and any notable rhythmic or melodic patterns. Submit your analysis as a plain text string, clearly separating each identified feature with a new line. Example format: 'Key: C major\nTime Signature: 4/4\nNotable patterns: [description]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = [
                "The melody should be coherent and musically pleasing.",
                "The melody should follow the given constraints (key, length, time signature, note range, rhythm)."
            ]
        else:
            criteria = [
                "The analysis should accurately identify the key features of the piece (key, time signature, notable patterns).",
                "The analysis should be clear, logically structured, and each feature should be separated by a new line."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

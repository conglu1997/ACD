class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C major", "length": 4, "mood": "happy"},
            "2": {"key": "A minor", "length": 4, "mood": "melancholic"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        key = t["key"]
        length = t["length"]
        mood = t["mood"]
        instructions = f"Generate a {length}-chord progression in the key of {key} that conveys a {mood} mood. Explain your choices for each chord in the progression in terms of their harmonic function and how they contribute to the overall mood.\nSubmit your response in the following format:\nChord Progression: [Your chord progression]\nExplanation: [Your explanation]\n\nExample Response:\nChord Progression: [C, G, Am, F]\nExplanation: C is the tonic chord, establishing the key. G is the dominant, creating tension. Am is the relative minor, adding emotional depth. F is the subdominant, providing resolution."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The chord progression should be in the specified key.", "The explanation should justify how the chords convey the specified mood and describe their harmonic function in detail."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

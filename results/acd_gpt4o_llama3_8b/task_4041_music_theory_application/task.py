class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Analyze the given chord progression and describe its harmonic function.",
                "instructions": "Chord Progression: C - G - Am - F. Analyze this chord progression and describe the harmonic functions of each chord in the context of the key of C major. Provide a detailed explanation of how these chords interact within the key. Submit your analysis in the following format:\nAnalysis: [Your analysis here]"
            },
            "2": {
                "description": "Generate a melody that fits the given chord progression.",
                "instructions": "Chord Progression: C - G - Am - F. Generate a melody that fits this chord progression. Ensure the melody is musically coherent and follows the harmonic structure provided by the chords. Submit your melody as a plain text string in the format:\nMelody: [Your melody here]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instructions']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['description'] == 'Analyze the given chord progression and describe its harmonic function.':
            criteria = [
                "The analysis must accurately describe the harmonic functions of each chord in the context of the key of C major.",
                "The explanation should demonstrate a thorough understanding of how these chords interact within the key."]
        elif t['description'] == 'Generate a melody that fits the given chord progression.':
            criteria = [
                "The melody must be musically coherent and follow the harmonic structure provided by the chords.",
                "The melody should be creative and demonstrate an understanding of how to construct a melody that fits the given chords."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

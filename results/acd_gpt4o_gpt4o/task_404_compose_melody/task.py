class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "joyful"},
            "2": {"theme": "melancholic"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to compose a short melody based on the following theme or mood. After composing the melody, provide a brief explanation of how the melody reflects the given theme or mood.

Theme/Mood: {t['theme']}

Your response should include:
1. The melody in a format that includes notes and rhythm (e.g., C4 quarter note, D4 half note, E4 eighth note, etc.).
2. A brief explanation of how the melody captures the essence of the given theme or mood.

Ensure your melody is creative and your explanation is comprehensive. Provide your response in plain text format. Here is an example format for your response:

Melody: C4 quarter note, D4 quarter note, E4 half note
Explanation: The melody starts with a rising sequence of notes, which gives it a joyful and uplifting feel.

Response format:
Melody: [Your melody in the specified format]
Explanation: [Your explanation]

Please ensure that your melody is original and not directly copied from any known pieces."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a melody with notes and rhythm.",
            "The explanation should clearly relate the melody to the given theme or mood."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

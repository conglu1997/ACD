class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"chords": "C - G - Am - F"},
            "2": {"chords": "Dm - G - C - F"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Identify the chord progression in the following sequence of chords:

Chords: {t["chords"]}

Your response should include the chord progression in Roman numeral notation (e.g., I - V - vi - IV) and a brief explanation of the progression.

Submit your response as a plain text string in the following format:

Chord Progression: [Roman numeral notation]
Explanation: [Brief explanation of the progression]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include the correct Roman numeral notation for the chord progression.",
            "The response should include a brief explanation of the progression."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

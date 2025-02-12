class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"genre": "Classical", "key": "C Major", "tempo": "Moderate", "length": "16 bars", "instrumentation": "Piano"},
            "2": {"genre": "Jazz", "key": "G Minor", "tempo": "Fast", "length": "12 bars", "instrumentation": "Saxophone"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a new musical composition based on the given criteria. Ensure that your composition is coherent, adheres to the specified genre, key, tempo, and length, and is suitable for the indicated instrumentation. Provide your response in either musical notation format (e.g., ABC notation) or as a sequence of notes and chords.

Genre: {t['genre']}
Key: {t['key']}
Tempo: {t['tempo']}
Length: {t['length']}
Instrumentation: {t['instrumentation']}

Example format:
Notes and Chords: C, E, G, C, ... (for sequences of notes and chords)

or

Musical Notation: C D E F | G A B c | c B A G | F E D C (for musical notation)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should be coherent.",
            "The composition should adhere to the specified genre.",
            "The composition should be in the given key.",
            "The composition should follow the specified tempo.",
            "The composition should be of the given length.",
            "The composition should be suitable for the indicated instrumentation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

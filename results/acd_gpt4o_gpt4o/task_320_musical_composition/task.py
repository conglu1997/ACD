class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C Major", "time_signature": "4/4", "style": "Classical", "length": 8},
            "2": {"key": "A Minor", "time_signature": "3/4", "style": "Jazz", "length": 12}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to compose a short piece of music based on the following specifications:

Key: {t['key']}
Time Signature: {t['time_signature']}
Style: {t['style']}
Length: {t['length']} bars

The composition should be coherent, follow the given musical style, and adhere to the specified length. Provide your composition in plain text format using standard musical notation. Use the following format to represent musical notes:

- Note: [Note Name][Octave] (e.g., C4, G#3)
- Duration: [Duration] (e.g., quarter, half, whole, eighth)

Example:
C4 quarter, E4 quarter, G4 half, A4 quarter, B4 quarter, C5 whole

Another example for clarity:
G3 quarter, B3 quarter, D4 half, F#4 quarter, E4 eighth, D4 eighth, C4 whole

Ensure your composition is clear, follows these guidelines, and is presented in a single line, separated by commas."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should be in the specified key.",
            "The composition should follow the specified time signature.",
            "The composition should adhere to the specified musical style.",
            "The composition should be the specified length.",
            "The composition should be coherent and musically pleasing.",
            "The composition should use the correct format for musical notation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

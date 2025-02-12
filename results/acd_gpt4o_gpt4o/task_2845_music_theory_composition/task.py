class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": {
                    "key": "C Major",
                    "time_signature": "4/4",
                    "structure": "AABA",
                    "length": "8 bars per section"
                }
            },
            "2": {
                "constraints": {
                    "key": "G Minor",
                    "time_signature": "3/4",
                    "structure": "ABACA",
                    "length": "4 bars per section"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to compose a piece of music based on the given constraints. Here are the specifics:

Key: {t['constraints']['key']}
Time Signature: {t['constraints']['time_signature']}
Structure: {t['constraints']['structure']}
Length: {t['constraints']['length']}

Instructions:
1. Compose a piece of music that adheres to the specified key, time signature, structure, and length.
2. Ensure that your composition is coherent and follows basic music theory principles, including proper note durations and harmony.
3. Provide your composition in a readable format, listing the notes (e.g., C4, D4) and their durations (e.g., quarter note, half note).
4. The composition should include both melody and harmony where applicable.

Example Response Format:
Composition:
Section A: C4 quarter, D4 quarter, E4 half | G4 quarter, A4 quarter, B4 half
Section B: E4 quarter, F4 quarter, G4 half | A4 quarter, B4 quarter, C5 half
Section A: C4 quarter, D4 quarter, E4 half | G4 quarter, A4 quarter, B4 half
Section A: C4 quarter, D4 quarter, E4 half | G4 quarter, A4 quarter, B4 half

Ensure that your composition is original, follows the given constraints, and is musically coherent."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The composition should adhere to the specified key.",
            "The composition should follow the specified time signature.",
            "The composition should adhere to the specified structure and length.",
            "The composition should be musically coherent and follow basic music theory principles.",
            "The composition should include proper note durations and harmony."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

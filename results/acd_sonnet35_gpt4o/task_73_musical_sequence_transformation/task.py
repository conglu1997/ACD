import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "sequence": "C4 E4 G4 C5",
                "operation": "inversion",
                "key": "C major",
                "axis": "C4"
            },
            "2": {
                "sequence": "D4 F#4 A4 C#5 D5",
                "operation": "retrograde_inversion",
                "key": "D major",
                "axis": "D4"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Given the musical sequence '{t['sequence']}' in the key of {t['key']}, perform a {t['operation']} transformation on it. Here's some context:\n\n- In music theory, notes are named A, B, C, D, E, F, G, repeating across octaves.\n- The number after a note (e.g., C4) represents the octave, with C4 being middle C on a piano.\n- In a major key, the notes follow the pattern: whole, whole, half, whole, whole, whole, half step.\n\nFollow these steps:\n\n1. Identify the notes in the sequence and their positions in the given key.\n2. Apply the {t['operation']} transformation:\n   - For 'inversion', mirror each note around the axis of {t['axis']}, preserving the original octave relationships. For example, if C4 is the axis, E4 would become A3, and G4 would become F4.\n   - For 'retrograde', reverse the order of the notes.\n   - For 'retrograde_inversion', first invert the sequence, then reverse the order.\n3. Write the resulting sequence using the same notation as the input (e.g., C4 for middle C).\n4. Explain the steps you took to transform the sequence, including any specific music theory concepts you applied.\n\nProvide your answer in the following format:\n\nTransformed sequence: [Your answer]\n\nExplanation: [Your detailed explanation]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The transformed sequence correctly applies the {t['operation']} operation to the original sequence.",
            "The explanation demonstrates a clear understanding of the musical concepts involved in the transformation.",
            "The answer uses correct music notation consistent with the input format, including octave numbers.",
            f"For inversion, the transformation is done around the axis of {t['axis']} while preserving original octave relationships.",
            "For retrograde_inversion, both inversion and reversal are correctly applied in the right order.",
            "The explanation includes references to specific music theory concepts such as intervals, scale degrees, or key signatures.",
            "The transformed sequence maintains the correct tonal relationships within the given key."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

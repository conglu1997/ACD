class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scale": "C major", "constraints": "8 notes, end on the tonic (C), no repeated notes."},
            "2": {"scale": "A minor", "constraints": "8 notes, use at least one note from each octave, no repeated notes."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a melody based on the given musical scale and constraints.

Scale: {t['scale']}
Constraints: {t['constraints']}

Provide your melody as a sequence of note names (e.g., C, D, E, F, G, A, B, C). Ensure that the melody adheres to the given constraints and uses only notes from the specified scale.

Response format:
Melody: [Your melody]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The melody should use only notes from the specified scale.",
            "The melody should adhere to the given constraints.",
            "The melody should be a valid sequence of musical notes."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

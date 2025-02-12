class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"key": "C major", "constraints": "Use at least one secondary dominant chord, include a ii-V-I progression."},
            "2": {"key": "A minor", "constraints": "Include a deceptive cadence, use at least one borrowed chord from the parallel major."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a chord progression based on the following key and constraints:

Key: {t['key']}
Constraints: {t['constraints']}

Ensure the chord progression is musically valid, adheres to the constraints, and is in the given key. Provide your response in plain text format, with each chord separated by a hyphen (e.g., C - G - Am - F)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The chord progression should be musically valid.", "The chord progression should adhere to the constraints.", "The chord progression should be in the given key."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"notation": "C E G", "theory": "transpose up a major third"},
            "2": {"notation": "A B C# E", "theory": "convert to a minor key, starting from A"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given musical notation and apply the specified theoretical concept to generate a new musical sequence.

Notation: {t['notation']}
Theory: {t['theory']}

Provide the new musical sequence in the format of note names separated by spaces, e.g., C D E."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The new sequence must accurately reflect the specified theoretical concept.",
            "The notation should be correct and follow musical conventions.",
            "The transformation should be correctly applied based on musical theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

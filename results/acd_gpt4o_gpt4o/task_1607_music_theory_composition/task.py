class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scale_type": "major", "starting_note": "C", "length": 8},
            "2": {"scale_type": "minor", "starting_note": "A", "length": 8}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a musical scale and compose a simple melody based on the given parameters:

Scale Type: {t['scale_type']}
Starting Note: {t['starting_note']}
Length: {t['length']} notes

Your response should include:
1. The generated musical scale in the format of note names separated by commas (e.g., C, D, E, F, G, A, B, C).
2. A simple melody composed using the generated scale, with the melody also provided in the format of note names separated by commas.

Ensure your response is accurate according to the given scale type and starting note, and that the melody is creative and follows musical conventions. The melody should be between 4 to 8 notes long and use only the notes from the generated scale."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated musical scale should be accurate according to the given scale type and starting note.",
            "The simple melody should use the notes from the generated scale.",
            "The melody should be between 4 to 8 notes long.",
            "The melody should be creative and follow musical conventions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

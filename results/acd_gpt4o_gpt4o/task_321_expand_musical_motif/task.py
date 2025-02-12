import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"motif": "C E G C"},
            "2": {"motif": "G B D G"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to expand the following musical motif into a longer piece of music. The expansion should maintain musical coherence and demonstrate an understanding of musical structure and theory.

Motif: {t['motif']}

Provide your expanded music piece in plain text format, using standard musical notation (e.g., C D E F G A B). Ensure that your expansion is at least 16 notes long and maintains a logical progression from the given motif.

Here is an example of how to format your response:
Expanded Music: C E G C D F A C G B D F"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The expanded music should be at least 16 notes long.",
            "The expansion should maintain coherence and logical progression from the given motif.",
            "The expansion should demonstrate an understanding of musical structure and theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

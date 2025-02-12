class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "A calm and relaxing melody",
                "constraints": "Use the key of C major and a 4/4 time signature. The piece should be 8 bars long. Use at least one occurrence of each of the following note durations: whole note, half note, quarter note, and eighth note."
            },
            "2": {
                "theme": "An energetic and upbeat tune",
                "constraints": "Use the key of G major and a 3/4 time signature. The piece should be 8 bars long. Use at least one occurrence of each of the following note durations: whole note, half note, quarter note, and eighth note."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a short piece of music based on the given theme and constraints:

Theme:
{t['theme']}

Constraints:
{t['constraints']}

Submit your composition as a sequence of musical notes in plaintext format. Use standard musical note notation such as C4 for middle C, D4 for the D above middle C, etc. Indicate note durations with W for whole note, H for half note, Q for quarter note, and E for eighth note. For example, C4Q, D4H, E4E, F4W.

Ensure your composition adheres to the given constraints and appropriately reflects the theme."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The composition should be in the specified key.",
            "The composition should follow the specified time signature.",
            "The composition should be 8 bars long.",
            "The composition should include at least one whole note, half note, quarter note, and eighth note.",
            "The composition should appropriately reflect the given theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

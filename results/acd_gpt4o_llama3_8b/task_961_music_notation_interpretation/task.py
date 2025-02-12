class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "A simple melody consisting of the notes C, D, E, F, G, A, B in 4/4 time signature."
            },
            "2": {
                "description": "A chord progression in the key of C major, including the chords C, G, Am, and F in 4/4 time signature."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following musical description and generate the corresponding music notation:

{t['description']}

Ensure that the music notation is accurate and follows standard musical notation conventions. The notation should be provided in plain text using the ABC notation format. Submit your response as a plain text string.

Example of ABC notation format for a C major scale:

X: 1
T: C Major Scale
M: 4/4
K: C
C D E F | G A B c ||

Note: Strictly adhere to the ABC notation format to ensure correct evaluation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The music notation should be accurate.",
            "The notation should follow standard musical notation conventions.",
            "The notation should be provided in ABC notation format.",
            "The submission should strictly adhere to the ABC notation format provided in the example."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

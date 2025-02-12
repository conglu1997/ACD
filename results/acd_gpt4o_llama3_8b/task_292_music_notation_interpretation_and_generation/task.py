class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "notation": "C4 Q, D4 Q, E4 H",
                "instruction": "Interpret the given music notation and describe the melody in plain text. The description should include the sequence of notes and their durations. For example: 'The melody consists of a quarter note C4, followed by a quarter note D4, and ends with a half note E4.'"
            },
            "2": {
                "instruction": "Generate music notation for a simple melody in the key of C major that is 4 bars long in 4/4 time signature. Ensure the melody is musically coherent and follows standard music notation rules. Format your response as a sequence of notes with their respective durations, e.g., 'C4 Q, D4 Q, E4 Q, F4 Q, G4 H'."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "notation" in t:
            return f"Interpret the following music notation and describe the melody in plain text. The description should include the sequence of notes and their durations.\n\nNotation: {t['notation']}"
        else:
            return "Generate music notation for a simple melody in the key of C major that is 4 bars long in 4/4 time signature. Ensure the melody is musically coherent and follows standard music notation rules. Format your response as a sequence of notes with their respective durations, e.g., 'C4 Q, D4 Q, E4 Q, F4 Q, G4 H'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "notation" in t:
            criteria = [
                "The description should accurately reflect the melody represented by the notation.",
                "The response should describe the sequence of notes and their durations accurately."
            ]
        else:
            criteria = [
                "The generated music notation should be in the key of C major.",
                "The melody should be 4 bars long in 4/4 time signature.",
                "The notation should be musically coherent and follow standard music notation rules."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

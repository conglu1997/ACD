class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "key": "C Major",
                "style": "Jazz"
            },
            "2": {
                "key": "A Minor",
                "style": "Blues"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a musical chord progression based on the given key and style. Ensure that your chord progression is coherent and follows the conventions of the specified style. For Jazz, you may include chords like maj7, min7, dom7, dim7, etc. For Blues, you may include chords like 7, 9, 11, etc. Submit your chord progression as a plain text string in the following format: [Chord 1] - [Chord 2] - [Chord 3] - [Chord 4].\n\nKey: {t['key']}\nStyle: {t['style']}\n\nExample submission: [Cmaj7] - [Dmin7] - [G7] - [Cmaj7]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The chord progression should be coherent and follow the conventions of the specified style.",
            "The chord progression should be in the given key."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

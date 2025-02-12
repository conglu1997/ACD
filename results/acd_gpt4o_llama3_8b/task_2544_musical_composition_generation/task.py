class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "genre": "Classical",
                "mood": "joyful",
                "instrumentation": "piano"
            },
            "2": {
                "genre": "Jazz",
                "mood": "melancholic",
                "instrumentation": "saxophone"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a short musical composition based on the following parameters:

Genre: {t['genre']}
Mood: {t['mood']}
Instrumentation: {t['instrumentation']}

The composition should be at least 16 bars long and should reflect the given genre, mood, and instrumentation. Additionally, it must include tempo, key signature, and dynamics. Provide an explanation of the choices you made in the composition, including how you achieved the specified mood and how you utilized the instrumentation. Submit your response as a plain text string in the following format:

Composition: [Your composition in musical notation or a descriptive format]
Explanation: [Your explanation of the choices made in the composition]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The composition should be at least 16 bars long.",
            "The composition should reflect the given genre, mood, and instrumentation.",
            "The composition should include tempo, key signature, and dynamics.",
            "The explanation should detail the choices made in achieving the specified mood and utilizing the instrumentation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "time",
                "provided_metaphor": "Time is a thief that steals moments."
            },
            "2": {
                "theme": "love",
                "provided_metaphor": "Love is a fire that burns brightly."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts:

1. Generate an original metaphor based on the given theme. The metaphor should be creative and not a commonly known expression, such as 'time flies' or 'love is blind.'
2. Interpret the provided metaphor to explain its meaning in detail. Your interpretation should be at least three sentences long and cover the implied meaning and relevant connotations.

Theme: {t['theme']}
Provided Metaphor: {t['provided_metaphor']}

Example Response Format:

Generated Metaphor: Time is a river that carries us forward.
Interpretation: This metaphor suggests that time is like a river, constantly moving forward and carrying us along with it. Just as a river flows and never stops, time continues to pass without pause. The metaphor conveys the unstoppable and continuous nature of time.

Submit your response as a plain text string in the following format:

Generated Metaphor: [Your original metaphor]
Interpretation: [A detailed explanation of the provided metaphor, including its implied meaning and any relevant connotations.]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated metaphor should be original, creative, and relevant to the given theme.",
            "The interpretation should clearly and comprehensively explain the meaning of the provided metaphor and be at least three sentences long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

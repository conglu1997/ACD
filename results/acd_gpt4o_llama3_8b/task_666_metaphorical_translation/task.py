class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "metaphor": "The world is a stage, and we are merely players."
            },
            "2": {
                "metaphor": "Time is a thief that steals our moments."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following metaphorical or symbolic language into a literal description or explanation. Ensure your translation captures the essence of the metaphor and conveys its meaning clearly and accurately.

Metaphor: {t['metaphor']}

Submit your translation as a plain text string in the following format:
Translation: [Your literal description or explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should accurately capture the essence of the metaphor.",
            "The translation should be clear and logically structured.",
            "The response should be in the correct format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

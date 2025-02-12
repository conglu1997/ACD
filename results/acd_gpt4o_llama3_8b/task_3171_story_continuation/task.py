class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "mystery",
                "style": "Agatha Christie",
                "starting_paragraph": "The clock struck midnight and the manor was enveloped in an eerie silence. Miss Marple sat by the fireplace, knitting thoughtfully as she pondered the curious events of the day."
            },
            "2": {
                "theme": "science fiction",
                "style": "Isaac Asimov",
                "starting_paragraph": "The year was 2150 and humanity had spread across the stars. Dr. Calvin stood before the council, her mind racing with the implications of the latest robotic development."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Continue the following story based on the given theme and writing style. Make sure that the continuation is coherent, maintains the original narrative voice, and aligns with the specified theme.

Theme: {t['theme']}
Style: {t['style']}

Starting Paragraph:
{t['starting_paragraph']}

Your continuation should be approximately 200-300 words. Submit your continuation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The continuation should be coherent and logically follow the starting paragraph.",
            "The continuation should maintain the original narrative voice and style.",
            "The continuation should align with the specified theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

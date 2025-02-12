class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Honesty",
                "instructions": "Create a fable that includes animals as characters and conveys a moral lesson about honesty."
            },
            "2": {
                "theme": "Perseverance",
                "instructions": "Create a fable that includes animals as characters and conveys a moral lesson about perseverance."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a fable based on the following theme: {t['theme']}. Your fable should include animals as characters and convey a clear moral lesson related to the theme. Ensure your story is coherent, logically structured, and culturally appropriate. The fable should be at least 200 words long and include a title. Submit your fable as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The fable should include animals as characters.",
            "The fable should convey a clear moral lesson related to the theme.",
            "The story should be coherent and logically structured.",
            "The fable should be culturally appropriate.",
            "The fable should be at least 200 words long.",
            "The fable should include a title."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_text": "Hello, how are you? I hope you are having a great day! The sun is shining brightly and the birds are singing.",
                "source_language": "English",
                "target_language": "Klingon",
                "context": "Klingon is a fictional language from the Star Trek universe, known for its guttural sounds and complex grammar."
            },
            "2": {
                "source_text": "A star shines on the hour of our meeting. May your path be ever green and golden.",
                "source_language": "English",
                "target_language": "Elvish",
                "context": "Elvish is a fictional language from the Lord of the Rings universe, created by J.R.R. Tolkien."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the following text from {t['source_language']} to {t['target_language']}:

{t['source_text']}

Context: {t['context']}

Submit your translation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translation should accurately convey the meaning of the source text.", "The translation should maintain the context provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

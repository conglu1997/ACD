class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dialect": "Scottish English",
                "topic": "Describe a typical day in a small Scottish village.",
                "example_phrase": "It's a braw bricht moonlicht nicht the nicht."
            },
            "2": {
                "dialect": "Southern American English",
                "topic": "Describe a family gathering during Thanksgiving.",
                "example_phrase": "Y'all come back now, ya hear?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a passage in the specified English dialect or accent.

Dialect: {t['dialect']}
Topic: {t['topic']}

Ensure that your passage includes the following example phrase: {t['example_phrase']}

Your passage should be at least 150 words long and accurately reflect the specified dialect or accent. Submit your passage as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The passage should accurately reflect the specified dialect or accent.",
            "The passage should include the example phrase.",
            "The passage should be at least 150 words long.",
            "The passage should be coherent and relevant to the specified topic."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

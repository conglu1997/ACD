class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "word_count": 100,
                "theme": "unexpected friendship",
                "elements": ["a lost dog", "a rainy day", "a child"]
            },
            "2": {
                "word_count": 150,
                "theme": "a surprising discovery",
                "elements": ["an old map", "a hidden room", "a forgotten secret"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a micro-story based on the following constraints:

- Maximum word count: {t['word_count']} words
- Theme: {t['theme']}
- Elements to include: {', '.join(t['elements'])}

Ensure that your story is coherent, engaging, and adheres to the given constraints. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            f"The story should be no more than {t['word_count']} words.",
            "The story should clearly follow the given theme.",
            "The story should include all specified elements.",
            "The story should be coherent and engaging."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

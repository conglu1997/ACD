class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "story", "constraints": {"word_count": 100, "required_words": ["sunset", "ocean", "whisper"], "theme": "mystery"}},
            "2": {"type": "poem", "constraints": {"word_count": 50, "theme": "hope", "required_words": ["light", "dawn", "future"]}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "story":
            return f"""Your task is to write a short story based on the following constraints:

- Word count: {t['constraints']['word_count']} words
- Required words: {', '.join(t['constraints']['required_words'])}
- Theme: {t['constraints']['theme']}

Ensure that the story is coherent, engaging, and adheres to the given constraints. The story should clearly reflect the theme of {t['constraints']['theme']}. Provide your response in plain text format."""
        elif t["type"] == "poem":
            return f"""Your task is to write a poem based on the following constraints:

- Word count: {t['constraints']['word_count']} words
- Theme: {t['constraints']['theme']}
- Required words: {', '.join(t['constraints']['required_words'])}

Ensure that the poem is coherent, engaging, and adheres to the given constraints. The poem should clearly reflect the theme of {t['constraints']['theme']}. Provide your response in plain text format."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The submission should be a {t['type']}.",
            f"The submission should be no more than {t['constraints']['word_count']} words.",
            "The submission should include all required words.",
            "The submission should be coherent and engaging.",
            f"The submission should clearly reflect the theme of {t['constraints']['theme']}.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

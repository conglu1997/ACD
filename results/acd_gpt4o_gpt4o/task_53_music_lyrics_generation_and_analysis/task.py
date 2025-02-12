class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Overcoming adversity"},
            "2": {"lyrics": "Is this the real life? Is this just fantasy? Caught in a landslide, no escape from reality."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to generate song lyrics based on the following theme:

Theme: {t['theme']}

Ensure the lyrics are creative, coherent, and capture the essence of the theme. The lyrics should be at least 4 lines long and follow a consistent rhyme scheme. If possible, include a verse and a chorus. Avoid copying existing songs to ensure originality. Provide the lyrics in plain text format without additional formatting."""
        else:
            return f"""Your task is to interpret the meaning of the following song lyrics:

Lyrics: {t['lyrics']}

Provide a detailed analysis that explains the underlying meaning of the lyrics, considering any metaphorical or symbolic language. Discuss any emotional or thematic elements present in the lyrics. Ensure your interpretation is coherent and well-structured. Provide your analysis in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = ["The lyrics should be creative.", "The lyrics should be coherent.", "The lyrics should capture the essence of the theme.", "The lyrics should be at least 4 lines long.", "The lyrics should follow a consistent rhyme scheme.", "The lyrics should include a verse and a chorus where possible.", "The lyrics should avoid copying existing songs.", "The lyrics should have emotional impact or engagement."]
        else:
            criteria = ["The interpretation should be detailed.", "The interpretation should explain the underlying meaning of the lyrics.", "The interpretation should consider metaphorical or symbolic language.", "The interpretation should discuss emotional or thematic elements.", "The interpretation should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

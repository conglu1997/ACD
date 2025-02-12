class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_language": "Spanish", "target_language": "English", "poem": "Verde que te quiero verde.\nVerde viento. Verdes ramas.\nEl barco sobre la mar\ny el caballo en la montaña."},
            "2": {"source_language": "French", "target_language": "English", "poem": "Il pleure dans mon coeur\nComme il pleut sur la ville;\nQuelle est cette langueur\nQui pénètre mon coeur?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_language = t["source_language"]
        target_language = t["target_language"]
        poem = t["poem"]
        return f"""Translate the following poem from {source_language} to {target_language}. Your translation should maintain the poetic form, style, cultural nuances, meter, and rhyme scheme of the original poem. Ensure that the translated poem captures the essence and emotions conveyed in the original language.

Note: Pay special attention to cultural references and idiomatic expressions to preserve the original poem's depth.

Original Poem:
{poem}

Example format of translation:
[Your translated poem here]

Example snippet:
Original: Verde que te quiero verde.
Translation: Green, how I want you green.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should maintain the poetic form and style of the original poem.",
            "The translation should accurately capture the cultural nuances and emotions conveyed in the original poem.",
            "The translation should preserve the meter and rhyme scheme of the original poem.",
            "The translated poem should be coherent and readable in the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

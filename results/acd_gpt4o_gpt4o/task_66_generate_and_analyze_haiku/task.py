class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a haiku about the changing seasons."},
            "2": {"haiku": "An old silent pond... / A frog jumps into the pond— / Splash! Silence again."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Your task is to generate a haiku based on the following prompt:

Prompt: {t['prompt']}

Ensure your haiku follows the traditional structure of three lines with a 5-7-5 syllable pattern. Provide your haiku in plain text format."""
        else:
            return f"""Your task is to analyze the following haiku and describe its structure and theme:

Haiku: {t['haiku']}

Ensure your analysis includes a discussion of the syllable pattern, imagery, and themes present in the haiku. Provide your analysis in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            criteria = ["The haiku should follow the 5-7-5 syllable structure.", "The haiku should be relevant to the given prompt."]
        else:
            criteria = ["The analysis should correctly identify the 5-7-5 syllable structure.", "The analysis should discuss the imagery and themes of the haiku."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

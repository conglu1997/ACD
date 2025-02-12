class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "The wind whispers secrets\nThrough the leaves of ancient trees\nEchoes of the past."},
            "2": {"theme": "nature", "style": "haiku"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'poem' in t:
            return f"""Your task is to interpret the following poem and explain its meaning, themes, and use of poetic devices. Provide your analysis in plain text format.

Poem: {t['poem']}

Your response should include:
1. The overall meaning of the poem.
2. The main themes presented in the poem.
3. An analysis of the poetic devices used (such as metaphor, simile, rhyme, meter, etc.).

Provide your response in the following format:
1. Meaning: [your interpretation]\n2. Themes: [identified themes]\n3. Poetic Devices: [analysis of devices]"""
        elif 'theme' in t and 'style' in t:
            return f"""Your task is to create a new poem based on the following theme and style.

Theme: {t['theme']}
Style: {t['style']} (A haiku is a three-line poem with a syllable pattern of 5-7-5.)

Ensure that your poem is meaningful, adheres to the given theme, and follows the specified style. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'poem' in t:
            criteria = [
                "The response should include an accurate interpretation of the poem's overall meaning.",
                "The analysis should identify the main themes of the poem.",
                "The analysis should correctly identify and explain the poetic devices used in the poem."
            ]
        else:
            criteria = [
                "The poem should adhere to the given theme.",
                "The poem should follow the specified style (e.g., haiku).",
                "The poem should be meaningful and creative."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

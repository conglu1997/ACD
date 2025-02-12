class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature"},
            "2": {"poem": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate: Rough winds do shake the darling buds of May, And summer's lease hath all too short a date:"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to generate a poem based on the following theme:

Theme: {t['theme']}

Ensure the poem is creative, coherent, and reflects the theme. Use appropriate poetic devices such as metaphors, similes, and imagery. Provide your poem in plain text format."""
        else:
            return f"""Your task is to analyze the following poem and identify the poetic devices used. Discuss how these devices contribute to the overall meaning and effect of the poem. Provide your analysis in plain text format.

Poem: {t['poem']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = ["The poem should be creative, coherent, and reflect the theme.", "The poem should use at least three different poetic devices such as metaphors, similes, and imagery appropriately."]
        else:
            criteria = ["The analysis should accurately identify at least three poetic devices.", "The analysis should discuss how the identified devices contribute to the poem's meaning and effect."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

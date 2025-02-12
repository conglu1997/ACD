class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "The world is too much with us; late and soon,\nGetting and spending, we lay waste our powers;\nLittle we see in Nature that is ours;\nWe have given our hearts away, a sordid boon!"},
            "2": {"theme": "The feeling of solitude amidst the bustling life of a modern metropolis, capturing the contrast between inner emptiness and outer chaos."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'poem' in t:
            return f"""Your task is to analyze the following poem:

{t['poem']}

Provide a detailed analysis of the poem, including:
1. Themes: Identify and discuss the central themes of the poem.
2. Stylistic Elements: Highlight the key stylistic elements used by the poet, such as imagery, meter, rhyme, and symbolism.
3. Emotional Impact: Describe the emotional impact of the poem and how the poet achieves this effect.

Provide your response in plain text format with the following structure:

1. Themes: [Your analysis]
2. Stylistic Elements: [Your analysis]
3. Emotional Impact: [Your analysis]"""
        else:
            return f"""Your task is to create an original poem based on the following theme:

Theme: {t['theme']}

Ensure that your poem is creative, evocative, and reflects the given theme. Provide your response in plain text format as a complete poem with a title. Your poem should be at least 12 lines long and include at least one metaphor and one simile."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'poem' in t:
            criteria = [
                "The analysis should identify and discuss the central themes.",
                "The analysis should highlight key stylistic elements.",
                "The analysis should describe the emotional impact of the poem and how it is achieved."
            ]
        else:
            criteria = [
                "The poem should be creative, evocative, and reflect the given theme.",
                "The poem should include at least one metaphor and one simile.",
                "The poem should be at least 12 lines long."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

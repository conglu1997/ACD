class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Generate a poem based on the given theme and style.",
                "instructions": "Theme: Nature. Style: Haiku. Generate a haiku that captures the beauty of nature. Ensure your haiku follows the traditional 5-7-5 syllable structure. Submit your poem as a plain text string in the format:\nHaiku: [Your haiku here]"
            },
            "2": {
                "description": "Interpret the meaning and themes of the following poem.",
                "instructions": "Poem: 'The Road Not Taken' by Robert Frost. Interpret the meaning and themes of the poem. Provide a detailed analysis of the poem's message, use of language, and any symbolism. Submit your interpretation as a plain text string in the format:\nInterpretation: [Your interpretation here]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return t['instructions']

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['description'] == 'Generate a poem based on the given theme and style.':
            criteria = [
                "The poem must follow the given theme and style.",
                "The haiku must follow the traditional 5-7-5 syllable structure.",
                "The poem should evoke emotions and capture the beauty of nature."]
        elif t['description'] == 'Interpret the meaning and themes of the following poem.':
            criteria = [
                "The interpretation must accurately reflect the poem's message and themes.",
                "The analysis should be detailed and demonstrate a deep understanding of the poem's use of language and symbolism.",
                "The interpretation should be logically consistent and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

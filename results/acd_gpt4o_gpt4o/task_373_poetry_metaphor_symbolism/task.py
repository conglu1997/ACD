class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"themes": "love and loss"},
            "2": {"poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "themes" in t:
            themes = t["themes"]
            instructions = f"""Your task is to generate a poem based on the following themes: {themes}.

Your poem should be at least 12 lines long and make use of metaphor and symbolism to convey the themes. The poem should be original, creative, and demonstrate a deep understanding of the themes.

Provide your poem in plain text format."""
        else:
            poem = t["poem"]
            instructions = f"""Your task is to analyze the following poem and discuss the use of metaphor and symbolism within it.

Poem: {poem}

In your analysis, you should:
1. Identify and explain at least two metaphors used in the poem.
2. Identify and explain at least two symbols used in the poem.
3. Discuss how the metaphors and symbols contribute to the overall meaning and themes of the poem.

Your analysis should be at least 300 words long and provide a detailed and well-structured examination of the poem. Each section should be clearly labeled and elaborated upon.

Provide your analysis in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "themes" in t:
            criteria = [
                "The poem should be at least 12 lines long.",
                "The poem should make use of metaphor and symbolism.",
                "The poem should be original and creative.",
                "The poem should demonstrate a deep understanding of the themes."]
        else:
            criteria = [
                "The analysis should identify and explain at least two metaphors.",
                "The analysis should identify and explain at least two symbols.",
                "The analysis should discuss how the metaphors and symbols contribute to the overall meaning and themes.",
                "The analysis should be at least 300 words long.",
                "The analysis should be detailed and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

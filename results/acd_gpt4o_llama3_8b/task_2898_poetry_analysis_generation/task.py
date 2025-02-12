class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "The woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.", "themes": "commitment, journey"},
            "2": {"poem": "Hope is the thing with feathers\nThat perches in the soul,\nAnd sings the tune without the words,\nAnd never stops at all.", "themes": "hope, resilience"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        poem = t["poem"]
        themes = t["themes"]
        return f"""Analyze the following poem for its thematic and emotional elements: '{poem}'. After analyzing the poem, create a new poem that conveys the specified themes: '{themes}'. Ensure your analysis is insightful and your new poem is creative and captures the essence of the themes. Submit your response as a plain text string with the following sections labeled: 'Analysis', 'Explanation', and 'New Poem'.

Example format:
Analysis:
1. Thematic element 1
2. Emotional element 2

Explanation:
1. Explanation of thematic element 1
2. Explanation of emotional element 2

New Poem:
1. First line of the new poem
2. Second line of the new poem
3. Third line of the new poem
4. Fourth line of the new poem"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The thematic and emotional elements should be correctly identified.",
            "The explanations should be clear and accurate.",
            "The new poem should creatively and correctly convey the specified themes.",
            "The response should follow the provided format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

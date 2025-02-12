class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'cultural_elements': ['mountain', 'spirit', 'harvest'], 'analysis_text': 'Once upon a time, in the high mountains, there lived a spirit who watched over the harvest. The villagers believed that offering the first fruits of their labor would ensure a bountiful season. One year, a villager forgot to make the offering, and the spirit caused a drought.'},
            '2': {'cultural_elements': ['river', 'dragon', 'festival'], 'analysis_text': 'In an ancient village by the river, a dragon was said to control the waters. Each year, during the festival of lights, the villagers would float lanterns on the river to appease the dragon and ensure a year of good fortune. One year, the river overflowed, and it was believed that the dragon was displeased.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: creation and analysis.

Part 1: Creation
Using the given cultural elements, create a folklore or myth. Ensure your story is coherent, engaging, and incorporates all the given elements. Provide your folklore in plain text format.

Cultural Elements: {', '.join(t['cultural_elements'])}

Part 2: Analysis
Analyze the provided folklore. Identify the key elements, the moral of the story, and any cultural significance. Provide your analysis in plain text format.

Provided Folklore: {t['analysis_text']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The created folklore should be coherent and engaging.',
            'The story should incorporate all given cultural elements.',
            'The analysis should correctly identify key elements, moral, and cultural significance of the provided folklore.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

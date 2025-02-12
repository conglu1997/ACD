class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "Whose woods these are I think I know.\nHis house is in the village though;\nHe will not see me stopping here\nTo watch his woods fill up with snow.\n\nMy little horse must think it queer\nTo stop without a farmhouse near\nBetween the woods and frozen lake\nThe darkest evening of the year.\n\nHe gives his harness bells a shake\nTo ask if there is some mistake.\nThe only other sound’s the sweep\nOf easy wind and downy flake.\n\nThe woods are lovely, dark and deep,\nBut I have promises to keep,\nAnd miles to go before I sleep,\nAnd miles to go before I sleep.", "question": "Interpret the theme and mood of the poem. Provide a detailed analysis of how the poet uses language and imagery to convey these aspects."},
            "2": {"theme": "loneliness", "constraints": ["The poem must be in free verse.", "It should consist of 12-16 lines.", "Use at least three different poetic devices (e.g., metaphor, simile, alliteration, etc.)."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "poem" in t:
            instructions = f"""Your task is to interpret the following poem:

{t['poem']}

Question: {t['question']}

Provide a detailed analysis of the theme and mood of the poem. Discuss how the poet uses language and imagery to convey these aspects. Ensure your response is thorough and well-supported with examples from the text.

Response format:
1. Analysis: [Your detailed interpretation here]"""
        else:
            instructions = f"""Your task is to create a poem based on the following theme and constraints:

Theme: {t['theme']}

Constraints: {', '.join(t['constraints'])}

Ensure your poem adheres to the given theme and constraints. Use creative and vivid language to express the theme, and incorporate at least three different poetic devices. Provide your poem in plain text format.

Response format:
1. Poem: [Your poem here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "poem" in t:
            criteria.append("The response should provide a detailed analysis of the theme and mood, supported with examples from the text.")
        else:
            criteria.append("The poem should adhere to the theme of loneliness and the given constraints, including the use of at least three different poetic devices.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

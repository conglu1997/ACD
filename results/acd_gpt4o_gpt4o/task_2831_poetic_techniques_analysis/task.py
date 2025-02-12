class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate. Rough winds do shake the darling buds of May, and summer's lease hath all too short a date.", "technique": "Identify the poetic techniques used in the given text and explain their effect."},
            "2": {"technique": "Create a four-line poem using a simile and alliteration. Ensure the poem is coherent and uses these techniques effectively. Highlight where the simile and alliteration are used."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'text' in t:
            return f"""Your task is to identify and explain the poetic techniques used in the given text.

Text:
{t['text']}

Provide a detailed explanation of the identified techniques and their effect on the overall meaning and aesthetics of the text. Your response should be in plain text format, clearly indicating each identified technique and its effect."""
        else:
            return f"""Your task is to create a four-line poem using the specified poetic techniques.

Techniques:
{t['technique']}

Ensure that your poem is coherent and effectively uses the specified techniques. Highlight where the simile and alliteration are used. Provide your poem in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'text' in t:
            criteria = [
                "The response should correctly identify the poetic techniques used in the text.",
                "The response should provide a clear and accurate explanation of the effect of each technique on the text.",
                "All identified techniques should be correct and relevant to the text."
            ]
        else:
            criteria = [
                "The poem should be coherent and use a simile and alliteration effectively.",
                "The poem should be creative and aesthetically pleasing.",
                "The poem should highlight where the simile and alliteration are used."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

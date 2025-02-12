class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "themes": "love and loss",
                "length": "at least 8 lines"
            },
            "2": {
                "themes": "nature and time",
                "length": "at least 8 lines"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a poem based on the following themes: {t['themes']}. The poem should be at least {t['length']} long. Ensure that the language is poetic and stylistically rich, using vivid imagery and emotional depth. The poem should reflect the themes in a coherent manner. After generating the poem, provide an explanation of the metaphorical or symbolic significance of the poem, illustrating how the themes are represented and any deeper meanings conveyed. The explanation should tie back directly to the themes in the poem.

Submit your response as a plain text string in the following format:

Poem:
[Your poem]

Explanation:
[Your explanation]

Example:

Poem:
Love's fragile whisper fades into the night,
A shadow's dance under the moon's pale light.
Once vibrant hearts now beat in silent grief,
Echoes of joy, now lost like autumn's leaf.
Memories linger, bittersweet and cold,
In dreams, the past forever will unfold.
Yet from this sorrow, strength and hope arise,
Love's legacy, eternal in our eyes.

Explanation:
The poem reflects themes of love and loss by portraying the transformation of vibrant emotions into silent grief, symbolized by the fading whisper and shadow's dance. The metaphor of autumn's leaf represents the fleeting nature of joy. Despite the sorrow, the poem concludes with a message of hope and strength, indicating the lasting impact of love."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem should be based on the given themes.",
            "The poem should meet the specified length.",
            "The explanation should clearly illustrate the metaphorical or symbolic significance of the poem, tying back directly to the themes.",
            "The submission should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

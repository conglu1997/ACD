class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "form": "sonnet",
                "topic": "the changing of seasons",
                "requirements": "A sonnet with 14 lines, composed in iambic pentameter, and following the rhyme scheme ABABCDCDEFEFGG."
            },
            "2": {
                "form": "haiku",
                "topic": "a peaceful morning",
                "requirements": "A haiku with 3 lines, following the syllable pattern 5-7-5."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a poem based on the following requirements:

Poetic Form: {t['form']}
Topic: {t['topic']}
Requirements: {t['requirements']}

Ensure that your poem is creative, adheres to the specified form, and accurately reflects the given topic. Pay close attention to the meter and syllable counts required by the form.

For a sonnet, iambic pentameter means each line should have 10 syllables, following an unstressed-stressed (da-DUM) pattern. The rhyme scheme should be ABABCDCDEFEFGG.

For a haiku, the three lines should follow the syllable pattern 5-7-5.

Submit your poem as a plain text string in the following format:

For a sonnet:
Line 1: [text]
Line 2: [text]
...
Line 14: [text]

For a haiku:
Line 1: [text]
Line 2: [text]
Line 3: [text]

Make sure to follow the specified format exactly and provide a creative and coherent poem."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The poem should adhere to the specified poetic form.",
            "The poem should follow the given rhyme scheme and meter (if applicable).",
            "The poem should accurately reflect the given topic.",
            "The poem should be creative and coherent.",
            "The response should follow the specified format precisely.",
            "The poem should adhere to the required syllable counts and meter."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

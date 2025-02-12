class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "Shall I compare thee to a summer's day? Thou art more lovely and more temperate: Rough winds do shake the darling buds of May, And summer's lease hath all too short a date:", "transformation": "Rewrite the poem in the style of Edgar Allan Poe, incorporating elements of suspense and darkness."},
            "2": {"poem": "Do not go gentle into that good night, Old age should burn and rave at close of day; Rage, rage against the dying of the light.", "transformation": "Rewrite the poem as a haiku, adhering to the 5-7-5 syllable structure and maintaining the theme of defiance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following poem and transform it according to the given criteria:

Poem: {t['poem']}

Transformation Requirement: {t['transformation']}

Your response should:
1. Maintain the original poem's theme and meaning.
2. Adhere to the specified style or form.
3. Incorporate elements relevant to the new style or form (e.g., suspense and darkness for Edgar Allan Poe).

Submit your transformed poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The transformed poem should maintain the original poem's theme and meaning.",
            "The transformed poem should adhere to the specified style or form.",
            "The transformed poem should incorporate elements relevant to the new style or form.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

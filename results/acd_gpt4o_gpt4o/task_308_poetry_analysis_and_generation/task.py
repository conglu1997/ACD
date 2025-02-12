class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;""",
                        "theme": "choices and their consequences",
                        "form": "free verse"},
            "2": {"poem": """Shall I compare thee to a summer's day?
Thou art more lovely and more temperate:
Rough winds do shake the darling buds of May,
And summer's lease hath all too short a date:""",
                        "theme": "the beauty of the beloved",
                        "form": "sonnet"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following poem and then generate an original poem based on the specified theme and form.

Analyze the given poem for its themes, structure, and literary devices. Then, generate an original poem based on the provided theme and form.

Poem:
{t['poem']}

Theme for original poem: {t['theme']}
Form for original poem: {t['form']}

Provide your response in the following format:

Analysis:
- Theme: [Your analysis of the theme]
- Structure: [Your analysis of the structure]
- Literary Devices: [Your analysis of the literary devices used]

Original Poem:
- [Your original poem]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should accurately identify the theme, structure, and literary devices of the given poem.",
            "The original poem should adhere to the specified theme and form.",
            "The original poem should demonstrate creativity and coherence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

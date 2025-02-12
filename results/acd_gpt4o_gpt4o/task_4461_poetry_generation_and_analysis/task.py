class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"form": "sonnet", "style": "Shakespearean"},
            "2": {"form": "haiku", "style": "traditional"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a poem in the specified form and style. Ensure that the poem adheres to the structural and stylistic requirements of the form.

Form: {t['form']}
Style: {t['style']}

Provide the poem in plain text format. Here are the requirements for each form:

Sonnet (Shakespearean):
- 14 lines
- Each line typically has 10 syllables
- Rhyme scheme: ABABCDCDEFEFGG

Haiku (Traditional):
- 3 lines
- Syllable pattern: 5-7-5
- Typically focuses on nature or seasons

Make sure the poem aligns with the specified form and style."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the structural requirements of the specified form.",
            "The poem should follow the stylistic conventions of the specified style.",
            "The poem should be coherent and meaningful within the given form and style." 
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "The beauty of nature",
                "structure": "Sonnet (Shakespearean)"
            },
            "2": {
                "theme": "The passage of time",
                "structure": "Haiku"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        structure = t["structure"]
        instructions = f"""Your task is to generate a poem based on the following theme and structure:

Theme: {theme}
Structure: {structure}

Details for the structures:
1. Shakespearean Sonnet: 14 lines with a rhyme scheme of ABABCDCDEFEFGG.
2. Haiku: 3 lines with a syllable pattern of 5-7-5.

Your response should include:
1. The poem.
2. An explanation of the choice of poetic devices used, such as metaphor, simile, alliteration, rhyme scheme, and imagery.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the given theme and structure.",
            "The Shakespearean Sonnet should have 14 lines with the correct rhyme scheme.",
            "The Haiku should have 3 lines with a 5-7-5 syllable pattern.",
            "The explanation should accurately describe the poetic devices used.",
            "The poem should be creative and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
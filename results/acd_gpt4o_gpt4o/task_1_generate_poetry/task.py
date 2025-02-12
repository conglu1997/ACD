class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "structure": "haiku"},
            "2": {"theme": "love", "structure": "sonnet"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        structure = t["structure"]
        instructions = f"""Your task is to write a poem based on the following theme and structure:

Theme: {theme}
Structure: {structure}

A haiku is a three-line poem with a syllable pattern of 5-7-5.
A sonnet is a fourteen-line poem typically written in iambic pentameter with a rhyme scheme of ABABCDCDEFEFGG.
Make sure your poem adheres to the given structure and theme. Provide your poem in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should follow the specified syllable pattern or rhyme scheme.",
            "The poem should reflect the given theme."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

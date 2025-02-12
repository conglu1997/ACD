class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could
To where it bent in the undergrowth;""",
                 "theme": "choice", "structure": "quatrain"},
            "2": {"poem": """Hope is the thing with feathers
That perches in the soul,
And sings the tune without the words,
And never stops at all,""",
                 "theme": "hope", "structure": "free verse"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        poem = t["poem"]
        theme = t["theme"]
        structure = t["structure"]
        instructions = f"""Your task is twofold: first, interpret the following poem and explain its meaning; second, generate an original poem based on the given theme and structure.

Poem:
{poem}

Theme: {theme}
Structure: {structure}

For the interpretation, provide a detailed analysis of the poem's meaning, themes, and any notable literary devices used. For the poem generation, ensure that your poem follows the specified theme and structure. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should be detailed and cover the poem's meaning, themes, and literary devices.",
            "The generated poem should adhere to the given theme and structure."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

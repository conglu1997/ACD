class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Autumn", "expected_structure": "A short poem with 4 lines"},
            "2": {"poem": """Two roads diverged in a yellow wood,
And sorry I could not travel both
And be one traveler, long I stood
And looked down one as far as I could""",
                        "interpretation": "The poem speaks about the choices we make in life and the paths we take."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to generate a poem based on the given theme. Here is the theme:
{t['theme']}
The poem should be short and consist of 4 lines."""
        elif 'poem' in t:
            return f"""Your task is to interpret the meaning of the given poem. Here is the poem:
{t['poem']}
Please provide a clear and concise interpretation of the poem in one or two sentences."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = ["The poem should be creative, coherent, and relevant to the theme.", "The poem should consist of exactly 4 lines."]
        elif 'poem' in t:
            criteria = ["The interpretation should accurately reflect the meaning of the poem."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

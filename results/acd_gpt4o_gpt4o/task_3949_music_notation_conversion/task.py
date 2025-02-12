class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sheet_music": "E F G A B C D E F G"},
            "2": {"abc_notation": "X:2\nT:Minor Scale\nM:4/4\nK:Am\nA B C D E F G A"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'sheet_music' in t:
            return f"""Your task is to convert the following sheet music into ABC notation:\n\nSheet Music:\n{t['sheet_music']}\n\nProvide your conversion in the following format:\n\nX:1\nT:Converted Music\nM:4/4\nK:C\n[Your converted ABC notation]\n\nEnsure that the notes and their order match the given sheet music."""
        elif 'abc_notation' in t:
            return f"""Your task is to convert the following ABC notation into sheet music:\n\nABC Notation:\n{t['abc_notation']}\n\nProvide your conversion as a sequence of notes in plain text format.\n\nEnsure that the notes and their order match the given ABC notation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if 'sheet_music' in t:
            criteria = ["The response should be a valid ABC notation.", "The notes and their order should match the given sheet music."]
        elif 'abc_notation' in t:
            criteria = ["The response should be a valid sequence of notes.", "The notes and their order should match the given ABC notation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

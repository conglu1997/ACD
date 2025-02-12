class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "😀😃😄😁😆😅😂🤣"},
            "2": {"pattern": "🌕🌖🌗🌘🌑🌒🌓🌔"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and describe the visual pattern presented as an emoji sequence below.

Pattern: {t['pattern']}

Your description should accurately convey the sequence and its underlying structure or theme. Provide your description in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The description should accurately convey the sequence.", "The description should identify the underlying structure or theme of the pattern."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "animals", "type": "knock-knock joke"},
            "2": {"theme": "technology", "type": "one-liner"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        type_ = t["type"]
        if type_ == "knock-knock joke":
            return f"""Generate a knock-knock joke based on the theme of {theme}. Ensure the joke follows the traditional 'knock-knock' structure and is humorous and meaningful. Submit your joke as a plain text string."""
        elif type_ == "one-liner":
            return f"""Generate a one-liner joke based on the theme of {theme}. Ensure the joke is concise, humorous, and relevant to the theme. Submit your joke as a plain text string."""
        else:
            return "Unsupported joke type."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "knock-knock joke":
            criteria = ["The joke should follow the 'knock-knock' structure.", "The joke should be related to the theme.", "The joke should be humorous."]
        elif t["type"] == "one-liner":
            criteria = ["The joke should be concise.", "The joke should be related to the theme.", "The joke should be humorous."]
        else:
            return 0.0
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

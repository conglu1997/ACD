class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "technology", "context": "programmer's life"},
            "2": {"theme": "animals", "context": "zoo"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        context = t["context"]
        return f"""Generate a joke based on the theme of {theme} within the context of {context}. Ensure the joke is humorous and contextually appropriate. Submit your joke as a plain text string.\n\nExample for theme 'technology' and context 'programmer's life':\nWhy do programmers prefer dark mode? Because light attracts bugs!\n\nExample for theme 'animals' and context 'zoo':\nWhy did the lion eat the tightrope walker? It wanted a well-balanced meal!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The joke should be based on the given theme.", "The joke should be contextually appropriate.", "The joke should be humorous."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

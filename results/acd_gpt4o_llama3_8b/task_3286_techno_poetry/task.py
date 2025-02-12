class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "quantum mechanics"},
            "2": {"theme": "artificial intelligence"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t['theme']
        return f"Compose a poem based on the theme of {theme}. Ensure that the poem is both technically accurate and creatively expressive. The poem should be between 100 and 150 words. Submit your poem as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should accurately reflect the technical theme.",
            "The poem should be creatively expressive.",
            "The poem should be between 100 and 150 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

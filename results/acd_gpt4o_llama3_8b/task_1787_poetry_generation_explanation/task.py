class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Write a sonnet about the changing seasons."},
            "2": {"prompt": "Write a haiku about the feeling of hope."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a poem based on the following theme or prompt and provide a detailed explanation of its meaning, themes, and emotions. Ensure that your poem is original, creative, and clearly related to the theme or prompt. The poem should follow the specified structure (e.g., sonnet, haiku). After generating the poem, provide a detailed explanation of its meaning and how it relates to the theme or prompt. Submit your response as a plain text string in the following format:\n\nPoem:\n[Your poem here]\n\nExplanation:\n[Your explanation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The poem should be original and creative.", "The poem should follow the specified structure.", "The explanation should clearly describe the meaning, themes, and emotions conveyed in the poem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
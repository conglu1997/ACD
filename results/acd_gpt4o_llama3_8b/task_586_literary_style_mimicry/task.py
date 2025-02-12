class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"style": "Shakespearean Sonnet", "prompt": "Write a sonnet about the changing seasons."},
            "2": {"style": "Hemingway's Prose", "prompt": "Write a short passage about a fisherman at sea."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        style = t["style"]
        prompt = t["prompt"]
        return f"""Write a piece of writing in the style of {style}. Follow the given prompt:

Prompt: {prompt}

Your writing should adhere to the tone, language, and structure typical of {style}. Ensure your piece is coherent and captures the essence of the style. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The writing should adhere to the tone, language, and structure typical of the specified literary style."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

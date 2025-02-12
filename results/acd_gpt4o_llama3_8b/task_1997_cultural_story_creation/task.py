class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"country": "Japan", "elements": ["cherry blossoms", "samurai", "tea ceremony"]},
            "2": {"country": "Brazil", "elements": ["Carnival", "Amazon rainforest", "football"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story that incorporates the following cultural elements from {t['country']}: {', '.join(t['elements'])}. Ensure that the story is coherent, creatively written, and accurately reflects the cultural aspects mentioned. The story should be between 200 and 500 words. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be between 200 and 500 words.", "The cultural elements must be integral to the plot."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

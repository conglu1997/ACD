class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"artwork": "The Starry Night by Vincent van Gogh"},
            "2": {"artwork": "The Persistence of Memory by Salvador Dalí"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret and describe the following artwork in detail:

Artwork: {t['artwork']}

Your description should include:
1. A detailed visual description of the artwork.
2. An interpretation of the artistic techniques used.
3. The historical and cultural context of the artwork.
4. The emotions and themes conveyed by the artwork.

Ensure your response is comprehensive, accurate, and insightful. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

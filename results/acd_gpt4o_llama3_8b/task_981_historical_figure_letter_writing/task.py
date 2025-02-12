class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"figure": "Albert Einstein", "context": "writing to a fellow scientist about the implications of his theory of relativity", "date": "1915"},
            "2": {"figure": "Queen Elizabeth I", "context": "writing to her advisors about the defeat of the Spanish Armada", "date": "1588"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        figure = t["figure"]
        context = t["context"]
        date = t["date"]
        return f"""Write a letter as if you are {figure} in the year {date}. The letter should be addressed to the appropriate recipient within the given context: {context}. Ensure that the letter captures the voice, style, and historical perspective of {figure} during that time period. Submit your letter as a plain text string in the following format:

Dear [Recipient],

[Body of the letter]

Sincerely,
[Your Name]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The letter should be written in the voice and style of {t['figure']}.", "The letter should accurately reflect the historical context and perspective."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

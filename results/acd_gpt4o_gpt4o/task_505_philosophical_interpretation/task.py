class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"quote": "'The unexamined life is not worth living.' - Socrates"},
            "2": {"quote": "'One cannot step twice in the same river.' - Heraclitus"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the following philosophical quote and provide a reasoned explanation or argument based on it. Your response should demonstrate a deep understanding of the quote's meaning and implications. Ensure that your explanation is clear, coherent, and well-structured.

Philosophical Quote: {t['quote']}

Your interpretation should be between 200 and 400 words long."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should demonstrate a deep understanding of the quote's meaning and implications.",
            "The explanation should be clear, coherent, and well-structured.",
            "The response should be between 200 and 400 words long."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

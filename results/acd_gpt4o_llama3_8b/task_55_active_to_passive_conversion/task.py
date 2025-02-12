class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The cat chased the mouse."},
            "2": {"sentence": "The committee will review the proposal next week."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        sentence = t['sentence']
        return f"""Convert the following active voice sentence into a passive voice sentence:

Active voice sentence: {sentence}

Ensure that the meaning remains the same and the sentence is grammatically correct. Submit your converted sentence as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

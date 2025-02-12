class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "quantum entanglement"},
            "2": {"concept": "genetic engineering"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t['concept']
        return f"""Generate a short science fiction story based on the following scientific principle or concept: {concept}.

Ensure that your story is coherent, imaginative, and scientifically plausible. The story should be between 300 and 500 words. Submit your story as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

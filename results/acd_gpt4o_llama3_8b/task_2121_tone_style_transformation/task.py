class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"original_text": "The sun set over the hills, casting a warm glow over the sleepy town below.", "target_tone": "mysterious"},
            "2": {"original_text": "The bustling city was alive with energy, people moving in every direction.", "target_tone": "nostalgic"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        original_text = t["original_text"]
        target_tone = t["target_tone"]
        return f"""Rewrite the following passage to match the specified tone or style:

Original Text: {original_text}
Target Tone/Style: {target_tone}

Ensure that the rewritten passage clearly reflects the desired tone or style while maintaining the original meaning. Submit your rewritten passage as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The rewritten passage should clearly reflect the target tone or style.", "The rewritten passage should maintain the original meaning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

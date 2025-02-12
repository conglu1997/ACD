class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"pattern": "⬜⬛⬜⬛⬛⬜⬛⬜⬜⬛", "continue": 4},
            "2": {"pattern": "▲▼▲▲▼▲▲▼▼", "continue": 3}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Recognize the pattern in the given sequence and continue it for the specified number of steps.

Pattern: {t['pattern']}
Continue for: {t['continue']} steps

Submit your response as a plain text string with the continued pattern. Ensure your response directly continues the given pattern without any additional text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should correctly continue the pattern for {t['continue']} steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

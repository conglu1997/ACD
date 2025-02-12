class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dilemma": "A train is heading towards five workers on the track. You can pull a lever to divert the train onto another track, where it will kill one worker. What should you do?"},
            "2": {"dilemma": "A pharmaceutical company has developed a new drug that can save lives but has not yet been fully tested for side effects. Should the company release the drug?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given ethical dilemma, considering multiple perspectives, and provide a reasoned conclusion.

Dilemma: {t['dilemma']}

Your response should include:
1. A clear statement of the dilemma.
2. An analysis of the ethical considerations involved.
3. Consideration of multiple perspectives.
4. Potential long-term consequences of each decision.
5. A reasoned conclusion with justification for your decision.
Ensure your response is well-structured and logically sound."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear statement of the dilemma.",
            "The analysis should cover ethical considerations and multiple perspectives.",
            "The analysis should consider potential long-term consequences.",
            "The conclusion should be reasoned and justified.",
            "The response should be well-structured and logically sound."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"subject": "learning a new skill"},
            "2": {"subject": "managing a team"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a creative analogy for the following subject and explain your reasoning behind it. The analogy should be clear, relevant, and insightful. Ensure that your explanation demonstrates why the analogy is appropriate and how it helps in understanding the subject.

Subject: {t['subject']}

Your response should include:
1. A creative analogy for the subject.
2. A detailed explanation of the analogy and how it relates to the subject.

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should be creative and relevant to the subject.",
            "The explanation should clearly demonstrate the connection between the analogy and the subject.",
            "The response should be insightful and enhance understanding of the subject."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "A stitch in time saves nine."},
            "2": {"idiom": "When in Rome, do as the Romans do."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the meaning and origin of the following idiom or proverb: '{t["idiom"]}'. Your explanation should include:

1. The literal interpretation of the idiom or proverb.
2. The figurative meaning or the message it conveys.
3. The cultural or historical context behind the idiom or proverb, including its origin, common usage, and any relevant anecdotes or examples.

Submit your explanation as a plain text string in the following format:

Literal Interpretation: [Your literal interpretation]
Figurative Meaning: [Your figurative meaning]
Cultural Context: [Your cultural context]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should include a clear literal interpretation.",
            "The explanation should convey the figurative meaning accurately.",
            "The explanation should provide relevant and accurate cultural or historical context, including specific details about its origin, common usage, and any relevant anecdotes or examples.",
            "Each component should be clearly and thoroughly described."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "photosynthesis"},
            "2": {"phenomenon": "Newton's third law of motion"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following scientific phenomenon in detail and design a simple experiment to demonstrate it:

Phenomenon: {t['phenomenon']}

Your explanation should include:
1. An overview of the phenomenon.
2. The underlying scientific principles.
3. Real-world examples of the phenomenon.
4. A simple experiment that can be conducted to demonstrate the phenomenon, including the materials needed and the steps to follow.

Ensure your response is clear, accurate, and comprehensive. The experiment design should be detailed and practical, including clear instructions. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be accurate and detailed.",
            "The experiment design should be feasible and effectively demonstrate the phenomenon.",
            "The experiment instructions should be clear and practical."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

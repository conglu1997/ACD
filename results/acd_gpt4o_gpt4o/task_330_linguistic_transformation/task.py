class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The quick brown fox jumps over the lazy dog.", "transformation": "Transform the sentence into passive voice."},
            "2": {"sentence": "She sells sea shells by the sea shore.", "transformation": "Transform the sentence into a question."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to transform the given sentence according to the specified linguistic rule or constraint.

Sentence: {t["sentence"]}
Transformation: {t["transformation"]}

Your response should accurately reflect the transformation specified. Provide your transformed sentence in plain text format without any additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The submission should accurately reflect the specified transformation.",
            "The submission should be a valid and grammatical sentence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

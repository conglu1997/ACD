class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"question": "Is free will an illusion?"},
            "2": {"question": "Can morality exist without religion?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        question = t['question']
        return f"""Analyze the following philosophical question: '{question}'. Present arguments both for and against the stance provided.
Ensure that your arguments are well-structured, logically coherent, and supported by relevant philosophical concepts or theories. Submit your response as a plain text string in the following format:

Arguments For: [Your arguments in favor]

Arguments Against: [Your arguments against]."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The arguments for the stance should be well-structured, logically coherent, and supported by relevant philosophical concepts or theories.",
            "The arguments against the stance should be well-structured, logically coherent, and supported by relevant philosophical concepts or theories."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

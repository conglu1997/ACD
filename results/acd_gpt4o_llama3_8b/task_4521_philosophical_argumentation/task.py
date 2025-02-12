class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Does free will exist?"},
            "2": {"prompt": "Is morality subjective or objective?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Generate a philosophical argument based on the following prompt: '{prompt}'

Your argument should be well-structured, logically sound, and demonstrate a deep understanding of the philosophical concepts involved. After presenting your argument, provide a critical evaluation of its strengths and weaknesses. Submit your response in the following format:

Argument:
[Your philosophical argument]

Evaluation:
[Your critical evaluation of the argument's strengths and weaknesses]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument must be well-structured and logically sound.",
            "The argument must demonstrate a deep understanding of the philosophical concepts involved.",
            "The evaluation must critically assess the strengths and weaknesses of the argument.",
            "The submission must be clear, coherent, and insightful.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

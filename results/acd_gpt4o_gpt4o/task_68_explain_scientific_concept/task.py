class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "Explain the process of photosynthesis in plants."},
            "2": {"concept": "Explain the theory of general relativity."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following scientific concept in detail:

{t["concept"]}

Make sure to cover the main points, use clear and concise language, and structure your explanation logically. Your explanation should be understandable to someone with a basic background in science. Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should cover the main points of the concept.",
            "The language used should be clear and concise.",
            "The explanation should be logically structured.",
            "The explanation should be understandable to someone with a basic background in science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

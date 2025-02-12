class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scientific_principle": "Quantum Entanglement"},
            "2": {"scientific_principle": "Black Holes"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to write a short science fiction story based on the following scientific principle: {t["scientific_principle"]}. Ensure that the story is creative, coherent, and incorporates the scientific principle accurately. The story should be between 300 and 500 words and should not exceed 500 words. Provide your story in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The story should be creative, coherent, and between 300 and 500 words.", "The scientific principle should be accurately and centrally incorporated into the story."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concepts": ["photosynthesis", "impressionist painting"]},
            "2": {"concepts": ["quantum mechanics", "classical music"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an explanation that connects the following concepts from different domains: {t["concepts"]}. Your explanation should be coherent, insightful, and demonstrate a clear understanding of both concepts. Aim to highlight any interesting parallels, contrasts, or interactions between them. Submit your response in prose format, not exceeding 500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be coherent.",
            "The explanation should demonstrate a clear understanding of both concepts.",
            "The explanation should highlight interesting parallels, contrasts, or interactions between the concepts.",
            "The explanation should not exceed 500 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

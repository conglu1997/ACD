class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "homeomorphism"},
            "2": {"concept": "compactness"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to explain the following topological concept in a clear and detailed manner, and provide at least one example to illustrate the concept. Ensure that your explanation is accurate and comprehensible to someone with a background in undergraduate mathematics.

Concept: {t['concept']}

Your response should include:
1. A clear and accurate definition of the concept.
2. A detailed explanation that breaks down the concept into understandable parts.
3. At least one example that illustrates the concept in practice.
4. Any relevant diagrams or visual aids that could help in understanding (described in text).

Provide your explanation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0

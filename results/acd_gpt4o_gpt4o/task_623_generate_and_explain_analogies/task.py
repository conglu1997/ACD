class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concepts": "Time and River"},
            "2": {"concepts": "Knowledge and Light"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate an analogy based on the following concepts and explain the relationship between them:

{t["concepts"]}

Your response should include:
1. The analogy.
2. A detailed explanation of how the concepts are related, considering any linguistic, contextual, or conceptual elements that contribute to the analogy.

Ensure your analogy is appropriate and your explanation is clear and insightful. Your explanation should cover the nature of the relationship between the concepts, any underlying similarities or differences, and the broader context that makes the analogy meaningful. Format your response in plain text."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an analogy based on the given concepts.",
            "The response should include a detailed explanation of how the concepts are related.",
            "The analogy should be appropriate and the explanation should be clear and insightful, covering the nature of the relationship between the concepts, any underlying similarities or differences, and the broader context that makes the analogy meaningful."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

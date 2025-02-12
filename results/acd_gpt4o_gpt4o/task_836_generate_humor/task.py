class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"setup": "Why did the scarecrow win an award?", "context": "The scarecrow was known for its excellent performance in the field. It had been standing tall and scaring away crows more effectively than any other in the region."},
            "2": {"setup": "Why don't scientists trust atoms?", "context": "Scientists often joke about the fundamental nature of atoms. They know that atoms make up everything, including the things that can't be trusted."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a humorous response based on the following setup and context:

Setup: {t['setup']}
Context: {t['context']}

Ensure the response is original, funny, contextually appropriate, and aligns with the setup provided. Avoid using well-known jokes or punchlines. Provide your response in plain text format without additional formatting."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should be original.", "The response should be funny.", "The response should be contextually appropriate.", "The response should align with the setup provided."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

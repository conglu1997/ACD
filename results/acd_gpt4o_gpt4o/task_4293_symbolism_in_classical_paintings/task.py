class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"painting": "The Ambassadors by Hans Holbein the Younger"},
            "2": {"painting": "The Garden of Earthly Delights by Hieronymus Bosch"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the symbolism in the following classical painting and provide an interpretation based on its historical and cultural context:

Painting: {t["painting"]}

Your response should include:
1. A brief description of the painting.
2. Identification of key symbolic elements in the painting.
3. An interpretation of these symbols based on historical and cultural context.
4. A well-structured explanation tying the symbols to the overall meaning of the painting.

Provide your response in plain text format, organized into clearly labeled sections as described above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a brief description of the painting.",
            "The response should identify key symbolic elements in the painting.",
            "The response should interpret these symbols based on historical and cultural context.",
            "The response should provide a well-structured explanation tying the symbols to the overall meaning of the painting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

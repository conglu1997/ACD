class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "The nature of time",
                "instructions": "Provide a detailed interpretation and analysis of the concept 'The nature of time'. Your analysis should include a philosophical viewpoint, potential implications, and real-world applications. Ensure your response is well-structured and logically sound. Submit your response as a plain text string, between 300 and 500 words."
            },
            "2": {
                "concept": "The essence of beauty",
                "instructions": "Provide a detailed interpretation and analysis of the concept 'The essence of beauty'. Your analysis should include a philosophical viewpoint, potential implications, and real-world applications. Ensure your response is well-structured and logically sound. Submit your response as a plain text string, between 300 and 500 words."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed interpretation and analysis of the concept '{t['concept']}'. Your analysis should include a philosophical viewpoint, potential implications, and real-world applications. Ensure your response is well-structured and logically sound. Submit your response as a plain text string, between 300 and 500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analysis should include a philosophical viewpoint.",
            "The analysis should mention potential implications.",
            "The analysis should discuss real-world applications.",
            "The response should be well-structured and logically sound.",
            "The response should be between 300 and 500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

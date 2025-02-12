class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Describe the cultural significance of the Renaissance period in Europe."
            },
            "2": {
                "prompt": "Explain the historical context and impact of the Industrial Revolution."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Provide a detailed response to the following prompt: {t['prompt']}. Your response should include key cultural or historical aspects, significant events or figures, and the broader impact on society. Ensure your explanation is comprehensive and accurate. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be comprehensive and accurate.",
            "The response should include key cultural or historical aspects.",
            "The response should mention significant events or figures.",
            "The response should discuss the broader impact on society."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

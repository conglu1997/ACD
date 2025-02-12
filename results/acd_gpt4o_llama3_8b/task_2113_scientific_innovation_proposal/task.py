class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "field": "renewable energy",
                "prompt": "Propose a new innovation in the field of renewable energy. Your proposal should include a detailed explanation of how the innovation works, the science behind it, and potential applications. Ensure your explanation is at least 300 words long."
            },
            "2": {
                "field": "biotechnology",
                "prompt": "Propose a new innovation in the field of biotechnology. Your proposal should include a detailed explanation of how the innovation works, the science behind it, and potential applications. Ensure your explanation is at least 300 words long."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Propose a new scientific innovation based on the given field. Your proposal should include a detailed explanation of how the innovation works, the science behind it, and potential applications. Ensure your explanation is at least 300 words long.

Field: {t['field']}
Prompt: {t['prompt']}

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be detailed and logically structured.",
            "The explanation should cover the science behind the innovation.",
            "The explanation should include potential applications.",
            "The explanation should be at least 300 words long."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

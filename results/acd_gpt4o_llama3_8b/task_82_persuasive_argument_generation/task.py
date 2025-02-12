class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The importance of environmental conservation",
                "instructions": "Generate a persuasive argument on the importance of environmental conservation."
            },
            "2": {
                "topic": "The benefits of a plant-based diet",
                "instructions": "Generate a persuasive argument on the benefits of a plant-based diet."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a persuasive argument on the following topic: {t['topic']}. Your argument should be convincing, logically structured, and use persuasive language. Ensure your argument includes the following sections: Introduction, Body, Conclusion. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument should be convincing.",
            "The argument should be logically structured.",
            "The argument should use persuasive language.",
            "The response should include sections for Introduction, Body, and Conclusion."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

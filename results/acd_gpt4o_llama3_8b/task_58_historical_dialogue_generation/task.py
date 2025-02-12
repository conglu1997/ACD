class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "figures": ["Leonardo da Vinci", "Albert Einstein"],
                "context": "Discussing the impact of scientific discoveries on art and society."
            },
            "2": {
                "figures": ["Cleopatra", "Queen Victoria"],
                "context": "Debating the challenges and responsibilities of ruling an empire."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a fictional dialogue between the following historical figures: {', '.join(t['figures'])}. The conversation should be contextually appropriate and reflect their unique perspectives. The context for the dialogue is: {t['context']}. Ensure that the dialogue is coherent, engaging, and historically accurate to the best of your ability. Submit the dialogue as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The dialogue should include all specified figures.",
            "The conversation should be contextually appropriate and reflect the unique perspectives of each figure.",
            "The dialogue should be coherent and engaging.",
            "The dialogue should be historically accurate to the best of your ability."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A friend just lost their beloved pet and is feeling devastated."
            },
            "2": {
                "scenario": "A colleague has been laid off unexpectedly and is worried about their future."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an empathetic and supportive response based on the following scenario:

Scenario: {t['scenario']}

Your response should be considerate, empathetic, and provide comfort or support relevant to the situation. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be empathetic and supportive.",
            "The response should be relevant to the scenario and provide comfort or support."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

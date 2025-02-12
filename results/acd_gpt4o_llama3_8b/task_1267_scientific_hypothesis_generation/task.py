class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Plants grow faster in red light compared to blue light."
            },
            "2": {
                "phenomenon": "A certain type of bacteria is resistant to a newly developed antibiotic."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a scientific hypothesis based on the following phenomenon: {t['phenomenon']}.

In addition to the hypothesis, propose an experimental setup to test it. Ensure that the hypothesis is logical and scientifically plausible. The experimental setup should include a clear description of the methodology, controls, variables, and expected outcomes. Submit your response as a plain text string in the following format:

Hypothesis: [Your hypothesis]
Experimental Setup: [Your experimental setup]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The hypothesis should be logical and scientifically plausible.",
            "The experimental setup should include a clear description of the methodology, controls, variables, and expected outcomes.",
            "The response should follow the format: 'Hypothesis: [Your hypothesis]\nExperimental Setup: [Your experimental setup]'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

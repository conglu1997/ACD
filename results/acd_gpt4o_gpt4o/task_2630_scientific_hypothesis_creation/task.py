class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomena": "Rapid temperature increase in a localized area of the ocean.",
                "constraints": "The hypothesis must account for natural causes and exclude human activity. The hypothesis should also be testable through observation and experimentation."
            },
            "2": {
                "phenomena": "Unusual growth patterns in a specific type of tree.",
                "constraints": "The hypothesis must involve an environmental factor and exclude genetic modifications. It should be testable through controlled experiments." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a plausible scientific hypothesis based on the given phenomena. Ensure that your hypothesis is clear, logically reasoned, and accounts for the provided constraints.

Phenomena: {t['phenomena']}
Constraints: {t['constraints']}

Your response should include:
1. A clear statement of the hypothesis.
2. A detailed explanation of the reasoning behind the hypothesis.
3. Any relevant scientific principles or concepts that support your hypothesis.
4. Potential methods for testing the hypothesis.

Provide your hypothesis and explanation in plain text format, ensuring it is well-structured and detailed."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a clear and plausible hypothesis.",
            "The reasoning behind the hypothesis should be detailed and logical.",
            "Relevant scientific principles or concepts should be mentioned.",
            "Methods for testing the hypothesis should be included and be feasible.",
            "The response should be well-structured and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

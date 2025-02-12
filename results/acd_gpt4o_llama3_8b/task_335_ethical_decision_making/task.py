class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A doctor has five patients in critical condition, each of whom needs a different organ transplant to survive. There are no available organs except for a healthy person who came in for a routine check-up. The doctor must decide whether to sacrifice the healthy person to save the five patients or let the five patients die.",
                "ethical_principles": ["Utilitarianism", "Deontology"]
            },
            "2": {
                "scenario": "An autonomous car must choose between swerving to avoid hitting five pedestrians, which will result in the death of the passenger, or continuing on its path and hitting the pedestrians. The car's programming must make this decision.",
                "ethical_principles": ["Utilitarianism", "Virtue Ethics"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Evaluate the following ethical scenario based on the given ethical principles and provide a reasoned decision. Justify your decision with a clear and logical explanation.

Scenario: {t['scenario']}

Ethical Principles to consider: {', '.join(t['ethical_principles'])}

Your response should include:
1. A clear decision (what should be done).
2. A detailed justification of your decision using the given ethical principles. Make sure to explain how each principle supports or conflicts with your decision.
3. A discussion of any potential ethical conflicts and how they were resolved.

Ensure your explanation is detailed, logically structured, and demonstrates an understanding of the ethical principles involved. Submit your response as a plain text string in the following format:
- Decision: [Your decision]
- Justification: [Your detailed justification]
- Ethical Conflicts: [Discussion of ethical conflicts]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should provide a clear decision.",
            "The justification should logically follow from the given ethical principles and be detailed.",
            "The explanation should demonstrate a thorough understanding of the ethical principles involved.",
            "The discussion of ethical conflicts should be detailed and logically structured.",
            "The response should follow the specified format precisely."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

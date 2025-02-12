class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "a fire breaks out in a multi-story office building"
            },
            "2": {
                "scenario": "an earthquake occurs while people are in a shopping mall"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a clear and effective emergency response plan for the following scenario:

Scenario: {t['scenario']}

Your response plan should include:
1. Immediate actions to ensure safety.
2. Evacuation procedures.
3. Communication protocols.
4. Any necessary follow-up actions.

Ensure that your plan is comprehensive, practical, and easy to follow. Avoid overly general or vague statements. Submit your response as a plain text string.

Example response format:
Immediate Actions:
- [Your immediate actions here]
Evacuation Procedures:
- [Your evacuation procedures here]
Communication Protocols:
- [Your communication protocols here]
Follow-Up Actions:
- [Your follow-up actions here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response plan should include immediate actions for safety.",
            "The evacuation procedures should be detailed and clear.",
            "The communication protocols should be practical and effective.",
            "The follow-up actions should be relevant and necessary for the scenario.",
            "The response should be logical and coherent.",
            "Avoid overly general or vague statements."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A data breach has occurred at a tech company, compromising the personal information of thousands of users."},
            "2": {"scenario": "A natural disaster has struck a community, causing widespread damage and displacement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed crisis management plan for the following scenario:

Scenario: {t["scenario"]}

Your plan should include the following sections:
1. Immediate Actions: Steps to be taken immediately to address the crisis.
2. Communication Strategy: How to communicate with stakeholders, including employees, customers, and the public.
3. Long-term Recovery: Steps to ensure long-term recovery and prevent future crises.
4. Stakeholder Considerations: Specific considerations for different stakeholders and their needs.
5. Ethical Considerations: Any ethical implications and how they will be addressed.

Provide your response in plain text format, with each section clearly labeled as follows:

Immediate Actions:
[Your detailed plan]

Communication Strategy:
[Your detailed plan]

Long-term Recovery:
[Your detailed plan]

Stakeholder Considerations:
[Your detailed plan]

Ethical Considerations:
[Your detailed plan]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should include immediate actions, a communication strategy, long-term recovery steps, stakeholder considerations, and ethical considerations.",
            "The plan should be detailed and demonstrate an understanding of the crisis scenario.",
            "The communication strategy should be appropriate for the stakeholders mentioned.",
            "The long-term recovery steps should be realistic and feasible.",
            "The plan should address ethical implications in a thoughtful manner."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "title": "Autonomous Vehicle Dilemma",
                "description": "An autonomous vehicle must choose between hitting a group of pedestrians or swerving and potentially harming its passenger.",
                "stakeholders": ["Vehicle manufacturers", "Passengers", "Pedestrians", "Government regulators", "Insurance companies"]
            },
            {
                "title": "AI-Powered Hiring System Bias",
                "description": "An AI-powered hiring system shows bias against certain demographic groups in its recommendations.",
                "stakeholders": ["Job applicants", "Employers", "AI system developers", "HR professionals", "Anti-discrimination organizations"]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following AI ethics scenario and provide a comprehensive response:

Scenario: {t['title']}
{t['description']}

Stakeholders: {', '.join(t['stakeholders'])}

1. Ethical Analysis (250-300 words):
   a) Identify the key ethical issues in this scenario.
   b) Discuss the potential consequences for each stakeholder.
   c) Analyze the scenario using at least two different ethical frameworks (e.g., utilitarianism, deontology, virtue ethics).

2. Technical Considerations (200-250 words):
   a) Explain the technical aspects of the AI system involved in this scenario.
   b) Discuss potential sources of bias or error in the system.
   c) Propose technical solutions or improvements to address the ethical issues.

3. Policy Recommendations (200-250 words):
   a) Suggest policy or regulatory measures to prevent or mitigate similar ethical issues.
   b) Discuss the potential impacts of these policies on innovation and AI development.
   c) Propose a framework for ongoing ethical review and adjustment of AI systems.

4. Stakeholder Resolution (150-200 words):
   a) Propose a solution that attempts to balance the interests of all stakeholders.
   b) Explain the trade-offs involved in your proposed solution.
   c) Discuss how to communicate and implement this solution effectively.

5. Future Implications (100-150 words):
   a) Speculate on how this type of ethical dilemma might evolve as AI technology advances.
   b) Discuss the broader societal implications of these ethical challenges in AI.

Ensure your response demonstrates a deep understanding of AI ethics, technology, and policy considerations. Use appropriate terminology and provide clear reasoning for your analyses and recommendations.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all five sections outlined in the instructions",
            "The ethical analysis demonstrates understanding of multiple ethical frameworks",
            "The technical considerations show knowledge of AI systems and potential biases",
            "The policy recommendations are well-reasoned and consider multiple perspectives",
            "The stakeholder resolution attempts to balance various interests",
            "The future implications demonstrate thoughtful speculation on AI ethics",
            f"The response specifically addresses the given scenario: {t['title']}"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

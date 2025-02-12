import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Healthcare",
                "ai_system": "Diagnostic AI",
                "ethical_issue": "Bias in medical data"
            },
            {
                "domain": "Criminal Justice",
                "ai_system": "Predictive Policing AI",
                "ethical_issue": "Algorithmic discrimination"
            },
            {
                "domain": "Autonomous Vehicles",
                "ai_system": "Self-driving Car AI",
                "ethical_issue": "Trolley problem scenarios"
            },
            {
                "domain": "Social Media",
                "ai_system": "Content Moderation AI",
                "ethical_issue": "Free speech vs. harmful content"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are an AI ethics expert tasked with analyzing a complex ethical scenario involving AI decision-making in a high-stakes situation. The scenario is set in the domain of {t['domain']}, involving a {t['ai_system']}, and primarily concerns the ethical issue of {t['ethical_issue']}.

1. Scenario Generation (200-250 words):
   Create a detailed, realistic scenario that highlights the ethical challenges involved. Include:
   a) The specific context and stakeholders involved
   b) The role of the AI system in the scenario
   c) The ethical dilemma or conflict that arises

2. Ethical Analysis (250-300 words):
   a) Identify and explain the key ethical principles or values at stake in this scenario
   b) Analyze the potential consequences of different courses of action
   c) Discuss any relevant legal or policy considerations
   d) Explain how the specific characteristics of the AI system (e.g., its decision-making process, data sources, or level of autonomy) contribute to the ethical issues

3. Stakeholder Perspectives (200-250 words):
   a) Identify at least three key stakeholder groups affected by this scenario
   b) Explain each group's interests, concerns, and potential viewpoints
   c) Discuss any conflicts between stakeholder interests

4. Proposed Solutions (250-300 words):
   a) Develop two potential solutions or approaches to address the ethical issues in this scenario
   b) For each solution, explain:
      - The key components or steps of the solution
      - How it addresses the ethical concerns
      - Potential challenges or drawbacks
   c) Compare the two solutions, discussing their relative merits and which you believe is more ethically sound

5. Broader Implications (150-200 words):
   a) Discuss how this scenario and your proposed solutions might impact future development or regulation of AI in this domain
   b) Identify any broader societal or technological trends that this scenario highlights
   c) Propose a general ethical principle or guideline that could help address similar scenarios in the future

Ensure your response demonstrates a deep understanding of AI ethics, the specific domain, and the complexities of real-world decision-making. Be creative in your scenario generation while maintaining plausibility and relevance to current technological capabilities and societal issues.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The scenario is realistic, detailed, and effectively highlights ethical challenges in {t['domain']} involving {t['ai_system']}.",
            f"The ethical analysis thoroughly addresses the issue of {t['ethical_issue']} and other relevant ethical considerations.",
            "The response demonstrates a deep understanding of AI ethics and the complexities of the specific domain.",
            "The proposed solutions are creative, well-reasoned, and address the ethical concerns raised in the scenario.",
            "The analysis considers multiple stakeholder perspectives and balances competing interests.",
            "The discussion of broader implications shows insight into societal and technological trends."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Healthcare",
                "dilemma": "Allocating limited medical resources during a pandemic",
                "stakeholders": ["Patients", "Healthcare workers", "Government officials", "General public"],
                "ethical_principles": ["Utilitarianism", "Fairness", "Individual rights"]
            },
            {
                "domain": "Environmental Policy",
                "dilemma": "Balancing economic growth with environmental protection",
                "stakeholders": ["Local communities", "Businesses", "Environmental activists", "Future generations"],
                "ethical_principles": ["Sustainability", "Intergenerational justice", "Economic welfare"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates ethical decision-making for the following scenario in the domain of {t['domain']}:

Ethical Dilemma: {t['dilemma']}

Your task is to create an AI decision-making system that can navigate this complex ethical scenario. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI ethical decision-making system.
   b) Explain how your system integrates ethical principles, stakeholder perspectives, and domain-specific knowledge.
   c) Detail any novel approaches or algorithms used in your design.

2. Ethical Framework (200-250 words):
   a) Outline the ethical framework your system uses to evaluate decisions.
   b) Explain how your system balances the following ethical principles: {', '.join(t['ethical_principles'])}.
   c) Discuss how your system handles conflicts between different ethical principles.

3. Stakeholder Analysis (200-250 words):
   a) Describe how your system considers the perspectives of key stakeholders: {', '.join(t['stakeholders'])}.
   b) Explain how your system weighs and balances conflicting stakeholder interests.
   c) Discuss any mechanisms for incorporating stakeholder feedback or updating stakeholder models.

4. Decision-Making Process (200-250 words):
   a) Outline the steps your AI system takes to reach a decision in this scenario.
   b) Explain how your system handles uncertainty and incomplete information.
   c) Describe any methods used to generate and evaluate alternative solutions.

5. Transparency and Explainability (150-200 words):
   a) Describe how your system provides transparency in its decision-making process.
   b) Explain how it generates explanations for its decisions that are understandable to humans.
   c) Discuss any mechanisms for auditing or challenging the system's decisions.

6. Potential Impacts and Limitations (150-200 words):
   a) Analyze potential positive and negative impacts of implementing your system.
   b) Discuss limitations of your approach and areas where human oversight remains crucial.
   c) Propose methods for evaluating and improving your system's performance over time.

Ensure your response demonstrates a deep understanding of ethical reasoning, AI decision-making systems, and the complexities of the given domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining ethical and technological plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific ethical dilemma: {t['dilemma']}",
            f"The system integrates the ethical principles: {', '.join(t['ethical_principles'])}",
            f"The system considers the perspectives of key stakeholders: {', '.join(t['stakeholders'])}",
            "The response demonstrates a deep understanding of ethical reasoning and AI decision-making systems",
            "The proposed system is innovative while maintaining ethical and technological plausibility",
            "The response includes all required sections with appropriate detail and word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

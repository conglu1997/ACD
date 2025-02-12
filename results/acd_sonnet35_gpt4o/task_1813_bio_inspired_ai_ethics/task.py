import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = ['neural networks', 'genetic algorithms', 'swarm intelligence', 'cellular automata']
        ai_applications = ['decision making', 'pattern recognition', 'autonomous systems', 'natural language processing']
        ethical_principles = ['fairness', 'transparency', 'privacy', 'accountability']
        societal_domains = ['healthcare', 'finance', 'education', 'environmental management']
        
        return {
            "1": {
                "biological_system": random.choice(biological_systems),
                "ai_application": random.choice(ai_applications),
                "ethical_principle": random.choice(ethical_principles),
                "societal_domain": random.choice(societal_domains)
            },
            "2": {
                "biological_system": random.choice(biological_systems),
                "ai_application": random.choice(ai_applications),
                "ethical_principle": random.choice(ethical_principles),
                "societal_domain": random.choice(societal_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a bio-inspired artificial intelligence system, focusing on ethical implications and potential societal impacts. Use the following specifications:

Biological System: {t['biological_system']}
AI Application: {t['ai_application']}
Ethical Principle: {t['ethical_principle']}
Societal Domain: {t['societal_domain']}

Your response should include the following sections:

1. System Design (250-300 words):
   a) Describe the key features and functioning of your bio-inspired AI system.
   b) Explain how it incorporates principles from the specified biological system.
   c) Detail how the system addresses the given AI application.
   d) Discuss any novel elements in your design that bridge biology and AI.

2. Biological-AI Integration (200-250 words):
   a) Analyze how specific biological mechanisms are translated into AI algorithms or architectures.
   b) Discuss the advantages and limitations of using this biological system as an inspiration for AI.
   c) Propose a specific experiment to validate the effectiveness of your bio-inspired approach.

3. Ethical Analysis (200-250 words):
   a) Examine the ethical challenges posed by your system, focusing on the specified ethical principle.
   b) Discuss any conflicts between the biological inspiration and ethical considerations.
   c) Propose two methods to address these ethical challenges, explaining their potential effectiveness and limitations.

4. Societal Impact (200-250 words):
   a) Analyze how your system could impact the specified societal domain.
   b) Provide two positive and two negative potential consequences, with at least one non-obvious example for each.
   c) Discuss how these impacts might evolve over time (5, 10, and 20 years).

5. Governance Framework (150-200 words):
   a) Propose a governance framework for regulating the development and use of your bio-inspired AI system.
   b) Include specific roles for government, industry, and civil society in your framework.
   c) Explain how your framework balances innovation with ethical concerns.

6. Future Directions (150-200 words):
   a) Suggest two potential advancements or modifications to your system that could enhance its capabilities or mitigate its risks.
   b) Discuss how your bio-inspired approach could be applied to other AI applications or societal domains.
   c) Speculate on how this type of bio-inspired AI might influence the broader field of AI research and development.

Ensure your response demonstrates a deep understanding of both biological systems and artificial intelligence principles, as well as a nuanced grasp of ethical reasoning and societal analysis. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes a bio-inspired AI system that incorporates principles from {t['biological_system']} and addresses {t['ai_application']}.",
            f"The ethical analysis thoroughly examines challenges related to {t['ethical_principle']} and proposes plausible solutions.",
            f"The societal impact analysis provides insightful positive and negative consequences for {t['societal_domain']}.",
            "The governance framework balances innovation with ethical concerns and includes roles for various stakeholders.",
            "The response demonstrates deep understanding of biological systems, AI principles, ethics, and societal analysis.",
            "The proposed system and analysis are innovative while maintaining scientific plausibility.",
            "The response addresses all required sections with appropriate detail and length.",
            "The total response is between 1150-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

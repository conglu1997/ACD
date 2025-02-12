import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        climate_variables = [
            'global temperature',
            'sea level rise',
            'extreme weather events',
            'biodiversity loss',
            'ocean acidification'
        ]
        ai_techniques = [
            'deep reinforcement learning',
            'federated learning',
            'explainable AI',
            'generative adversarial networks',
            'quantum machine learning'
        ]
        governance_challenges = [
            'international cooperation',
            'economic impact',
            'energy transition',
            'climate justice',
            'technological disparities'
        ]
        tasks = [
            {
                'climate_variable': random.choice(climate_variables),
                'ai_technique': random.choice(ai_techniques),
                'governance_challenge': random.choice(governance_challenges)
            },
            {
                'climate_variable': random.choice(climate_variables),
                'ai_technique': random.choice(ai_techniques),
                'governance_challenge': random.choice(governance_challenges)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered global climate governance system that integrates advanced climate modeling with policy decision-making to address climate change on a global scale. Your system should focus on modeling and mitigating {t['climate_variable']}, incorporate {t['ai_technique']} as a key AI component, and address the governance challenge of {t['governance_challenge']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-powered climate governance system.
   b) Explain how your system integrates climate modeling, AI decision-making, and global policy implementation.
   c) Detail how {t['ai_technique']} is utilized in your system design.
   d) Discuss how your system addresses the specific challenge of {t['governance_challenge']}.

2. Climate Modeling and Prediction (250-300 words):
   a) Explain how your system models and predicts changes in {t['climate_variable']}.
   b) Describe the data sources and types of data your system would use.
   c) Discuss how AI enhances the accuracy and speed of climate predictions in your system.

3. Policy Decision-Making Process (250-300 words):
   a) Outline how your system translates climate model outputs into policy recommendations.
   b) Explain how {t['ai_technique']} is used in the decision-making process.
   c) Describe mechanisms for balancing global and local interests in policy formation.

4. Implementation and Adaptation (200-250 words):
   a) Propose a method for implementing policies on a global scale.
   b) Describe how your system monitors policy effectiveness and adapts over time.
   c) Discuss potential challenges in global adoption and how your system addresses them.

5. Ethical Considerations and Safeguards (150-200 words):
   a) Identify potential ethical issues in using AI for global climate governance.
   b) Propose safeguards to ensure fairness, transparency, and accountability.
   c) Discuss how your system balances human oversight with AI-driven decision-making.

6. Future Developments and Implications (150-200 words):
   a) Suggest two potential advancements or extensions of your system.
   b) Discuss the broader implications of AI-driven global governance for international relations and sovereignty.

Ensure your response demonstrates a deep understanding of climate science, artificial intelligence, and global governance principles. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and political plausibility. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of climate science, artificial intelligence (particularly {t['ai_technique']}), and global governance principles.",
            f"The system architecture effectively integrates climate modeling, AI decision-making, and global policy implementation, with a clear focus on {t['climate_variable']}.",
            f"The climate modeling and prediction component is well-designed and utilizes AI to enhance accuracy and speed.",
            f"The policy decision-making process effectively translates climate model outputs into actionable recommendations, utilizing {t['ai_technique']}.",
            f"The implementation and adaptation section provides a plausible method for global policy implementation and system adaptation.",
            f"The response addresses the governance challenge of {t['governance_challenge']} throughout the system design.",
            "Ethical considerations and safeguards are thoroughly discussed, with clear proposals for ensuring fairness, transparency, and accountability.",
            "The response is innovative while maintaining scientific and political plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

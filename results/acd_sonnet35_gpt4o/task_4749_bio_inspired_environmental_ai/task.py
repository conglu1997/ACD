import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {'name': 'coral reef', 'key_feature': 'distributed sensing and communication'},
            {'name': 'rainforest canopy', 'key_feature': 'multi-level information processing'},
            {'name': 'soil microbiome', 'key_feature': 'adaptive resource allocation'}
        ]
        ai_architectures = ['neural network', 'evolutionary algorithm', 'swarm intelligence']
        environmental_challenges = [
            {'name': 'ocean acidification', 'data_type': 'pH levels and marine species populations'},
            {'name': 'deforestation', 'data_type': 'satellite imagery and biodiversity indices'},
            {'name': 'climate change', 'data_type': 'temperature, precipitation, and greenhouse gas levels'}
        ]
        
        tasks = [
            {
                'biological_system': random.choice(biological_systems),
                'ai_architecture': random.choice(ai_architectures),
                'environmental_challenge': random.choice(environmental_challenges)
            },
            {
                'biological_system': random.choice(biological_systems),
                'ai_architecture': random.choice(ai_architectures),
                'environmental_challenge': random.choice(environmental_challenges)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired AI system that mimics the information processing capabilities of a {t['biological_system']['name']} to analyze and interpret environmental data for ecosystem monitoring and predicting the effects of {t['environmental_challenge']['name']}. Your system should primarily use a {t['ai_architecture']} approach. Your response should include:

1. Biological System Analysis (250-300 words):
   a) Describe the key information processing features of the {t['biological_system']['name']}, focusing on its {t['biological_system']['key_feature']}.
   b) Explain how these features could be applied to environmental data analysis.
   c) Discuss any unique advantages this biological system might offer for monitoring {t['environmental_challenge']['name']}.

2. AI System Design (300-350 words):
   a) Outline the architecture of your bio-inspired AI system, detailing its main components.
   b) Explain how your system incorporates the {t['ai_architecture']} approach.
   c) Describe how your system mimics the {t['biological_system']['key_feature']} of the {t['biological_system']['name']}.
   d) Provide a high-level diagram or pseudocode illustrating your system's architecture.

3. Data Processing and Analysis (250-300 words):
   a) Describe how your system would process and analyze {t['environmental_challenge']['data_type']}.
   b) Explain how your system would use this data to monitor ecosystem health and predict {t['environmental_challenge']['name']} effects.
   c) Discuss any novel data interpretation techniques inspired by the {t['biological_system']['name']}.

4. Predictive Capabilities (200-250 words):
   a) Explain how your system would generate predictions related to {t['environmental_challenge']['name']}.
   b) Describe the potential accuracy and limitations of these predictions.
   c) Compare your bio-inspired approach to traditional methods of environmental modeling.

5. Implementation and Challenges (200-250 words):
   a) Discuss the technical challenges in implementing your system.
   b) Propose solutions to these challenges.
   c) Describe how you would validate and test your system's performance.

6. Ethical Considerations and Broader Impacts (150-200 words):
   a) Discuss potential ethical issues related to using bio-inspired AI for environmental monitoring.
   b) Explore the broader implications of your system for environmental science and policy.
   c) Suggest guidelines for the responsible development and use of such systems.

Ensure your response demonstrates a deep understanding of biology, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1650 words. Include a word count at the end of your submission.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response follows the structure specified in the instructions, including clear headings and numbered paragraphs.",
            f"The biological system analysis demonstrates a deep understanding of the {t['biological_system']['name']}'s information processing capabilities, particularly its {t['biological_system']['key_feature']}.",
            f"The AI system design effectively incorporates bio-inspired elements from the {t['biological_system']['name']} and uses a {t['ai_architecture']} approach.",
            f"The data processing and analysis section presents novel techniques for handling {t['environmental_challenge']['data_type']} inspired by the {t['biological_system']['name']}.",
            f"The predictive capabilities for {t['environmental_challenge']['name']} are well-explained and compared to traditional methods.",
            "Implementation challenges and potential solutions are thoroughly discussed, including validation and testing methods.",
            "Ethical considerations and broader impacts are thoughtfully explored, with specific guidelines proposed.",
            "The response demonstrates interdisciplinary knowledge integration across biology, AI, and environmental science.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word limits (1350-1650 words) and fully addresses all required components."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            ('coral reef', 'ocean acidification'),
            ('rainforest', 'deforestation'),
            ('arctic tundra', 'permafrost thaw'),
            ('grassland', 'invasive species')
        ]
        blockchain_features = [
            'smart contracts',
            'decentralized autonomous organizations (DAOs)',
            'non-fungible tokens (NFTs)',
            'zero-knowledge proofs'
        ]
        tasks = [
            {
                'ecosystem': eco[0],
                'environmental_threat': eco[1],
                'blockchain_feature': feature
            }
            for eco in ecosystems
            for feature in blockchain_features
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a blockchain-based system for real-time monitoring and management of a {t['ecosystem']} ecosystem, focusing on the threat of {t['environmental_threat']}. Your system should incorporate {t['blockchain_feature']} as a key blockchain technology. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your blockchain-based ecosystem monitoring system.
   b) Explain how it integrates IoT sensors, blockchain technology, and ecological modeling.
   c) Detail how {t['blockchain_feature']} is implemented in your system, including specific technical aspects.
   d) Include a simple diagram of your system architecture (described in text).

2. Data Collection and Validation (200-250 words):
   a) Describe the types of data collected by your system and the sensors used.
   b) Explain how data is validated and added to the blockchain, detailing the consensus mechanism.
   c) Discuss any novel approaches to ensure data integrity and reliability.
   d) Provide a specific example of how a data point would be processed in your system.

3. Ecosystem Modeling and Prediction (200-250 words):
   a) Explain how your system models the {t['ecosystem']} ecosystem, specifying the algorithms or approaches used.
   b) Describe how it predicts and monitors the impact of {t['environmental_threat']}.
   c) Discuss how blockchain technology enhances the modeling and prediction process.
   d) Provide a concrete example of how your system would predict a specific ecological change.

4. Intervention Mechanisms (200-250 words):
   a) Describe how your system triggers and manages interventions to address {t['environmental_threat']}.
   b) Explain the role of {t['blockchain_feature']} in the intervention process, including technical details.
   c) Discuss any ethical considerations in automated ecosystem management.
   d) Provide an example scenario of how your system would intervene in a critical situation.

5. Stakeholder Engagement (150-200 words):
   a) Identify key stakeholders for your system (e.g., scientists, local communities, governments).
   b) Explain how these stakeholders interact with and benefit from the system.
   c) Discuss how {t['blockchain_feature']} facilitates stakeholder engagement.
   d) Describe a use case demonstrating stakeholder interaction with your system.

6. Challenges and Future Developments (150-200 words):
   a) Identify key technical and practical challenges in implementing your system.
   b) Propose solutions or areas for future research to address these challenges.
   c) Suggest potential expansions or applications of your system to other ecological issues.

Ensure your response demonstrates a deep understanding of blockchain technology, ecology, and data science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section, including the word count at the end of each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of blockchain technology, ecology, and data science, particularly in relation to {t['ecosystem']} ecosystems and {t['environmental_threat']}.",
            f"The proposed system effectively integrates {t['blockchain_feature']} as a key blockchain technology in the context of ecosystem monitoring and management, with clear technical explanations.",
            "The response addresses all required sections with appropriate depth and creativity, adhering to the specified word counts.",
            "The proposed system is innovative while maintaining scientific and technological plausibility.",
            "The response includes a clear and logical diagram or description of the system architecture.",
            "The ethical implications and challenges of implementing such a system are thoroughly considered.",
            "Specific examples and use cases are provided to illustrate the system's functionality and stakeholder engagement.",
            "The response demonstrates a clear understanding of consensus mechanisms and data validation in blockchain systems.",
            "The ecosystem modeling approach is well-explained and technically sound.",
            "The intervention mechanisms are clearly described and ethically considered."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "region": "Sub-Saharan Africa",
                "climate_challenge": "Increasing drought frequency",
                "quantum_technique": "Quantum annealing",
                "timeframe": "30 years"
            },
            {
                "region": "Southeast Asia",
                "climate_challenge": "Rising sea levels",
                "quantum_technique": "Quantum machine learning",
                "timeframe": "50 years"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system for optimizing global food production and distribution in the face of climate change, focusing on {t['region']} and addressing the challenge of {t['climate_challenge']}. Your system should utilize {t['quantum_technique']} and project outcomes over a {t['timeframe']} period. Then, analyze its potential impact on food security and global economics. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-enhanced AI system for food production optimization.
   b) Explain how classical and quantum components interact in your design.
   c) Detail how your system incorporates {t['quantum_technique']} to enhance food production and distribution planning.
   d) Discuss how the system integrates climate models, agricultural data, and economic factors.

2. Quantum-Classical Integration (250-300 words):
   a) Explain how your system leverages {t['quantum_technique']} to process agricultural and climate data.
   b) Describe any novel algorithms or techniques your system uses to bridge quantum and classical computations.
   c) Discuss how this integration improves food production optimization compared to classical methods.

3. Climate Adaptation Strategies (250-300 words):
   a) Describe how your system develops strategies to adapt food production to {t['climate_challenge']} in {t['region']}.
   b) Explain how the system balances short-term production needs with long-term sustainability.
   c) Discuss any innovative agricultural techniques or technologies your system might propose.

4. Global Food Distribution Optimization (200-250 words):
   a) Explain how your system optimizes global food distribution to enhance food security.
   b) Describe how the system accounts for factors such as transportation, storage, and trade policies.
   c) Discuss how your system might help reduce food waste and improve resource allocation.

5. Economic Impact Analysis (200-250 words):
   a) Analyze the potential economic impacts of implementing your system's recommendations.
   b) Discuss how it might affect global food prices, trade patterns, and agricultural employment.
   c) Consider potential economic winners and losers from the proposed changes.

6. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss ethical implications of using quantum AI to guide global food production and distribution.
   b) Analyze potential societal impacts, including effects on rural communities and traditional farming practices.
   c) Propose guidelines for responsible implementation of this technology in global agriculture.

7. Limitations and Future Research (150-200 words):
   a) Identify potential limitations or challenges in implementing your proposed system.
   b) Suggest areas for future research to enhance the system's capabilities or address its limitations.
   c) Discuss how advancements in quantum computing might further improve the system in the coming decades.

Ensure your response demonstrates a deep understanding of quantum computing, artificial intelligence, climate science, agriculture, and global economics. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, artificial intelligence, climate science, agriculture, and global economics.",
            "The system architecture effectively integrates quantum and classical components for food production optimization.",
            "The proposed solution addresses the specified climate challenge and region appropriately.",
            "The response includes innovative approaches to food production and distribution optimization.",
            "The economic impact analysis is comprehensive and considers global implications.",
            "Ethical considerations and societal impacts are thoroughly discussed.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

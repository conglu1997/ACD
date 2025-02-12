import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem": "Amazon rainforest",
                "indigenous_group": "Kayapo people",
                "environmental_challenge": "deforestation and biodiversity loss"
            },
            {
                "ecosystem": "Arctic tundra",
                "indigenous_group": "Inuit",
                "environmental_challenge": "climate change and melting permafrost"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates indigenous ecological knowledge from the {t['indigenous_group']} with scientific data to predict and address {t['environmental_challenge']} in the {t['ecosystem']}. Your system should use natural language processing to analyze oral traditions and narratives. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system.
   b) Explain how it integrates natural language processing with environmental data analysis.
   c) Detail the data sources and types your system will use (both indigenous knowledge and scientific data).
   d) Discuss any novel techniques or algorithms used in your system.

2. Indigenous Knowledge Integration (200-250 words):
   a) Explain how your system will collect and process indigenous ecological knowledge.
   b) Describe techniques for preserving the cultural context and nuances of this knowledge.
   c) Discuss ethical considerations and protocols for working with indigenous communities.

3. Prediction and Analysis Mechanisms (200-250 words):
   a) Detail how your system will generate predictions about environmental changes.
   b) Explain how it will reconcile potential discrepancies between indigenous knowledge and scientific data.
   c) Describe the output format of your system's predictions and analyses.

4. Case Study (200-250 words):
   a) Provide a specific example of how your system would analyze a particular environmental indicator.
   b) Walk through the process from data input to prediction output.
   c) Explain how indigenous knowledge contributes to the analysis in this case.

5. Potential Applications and Impacts (150-200 words):
   a) Discuss potential applications of your system in environmental management and conservation.
   b) Analyze how this technology could benefit indigenous communities and global environmental efforts.
   c) Address any potential negative impacts or misuse of the system.

Ensure your response demonstrates a deep understanding of AI, natural language processing, environmental science, and indigenous knowledge systems. Use appropriate terminology and provide clear explanations. Be creative in your approach while maintaining scientific and ethical integrity.

Your total response should be between 1000-1250 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI, NLP, and environmental science",
            "The proposed system effectively integrates indigenous knowledge with scientific data",
            "The design shows creativity and innovation while maintaining scientific plausibility",
            "The response addresses ethical considerations and cultural sensitivity",
            "The case study provides a clear and realistic example of the system's application",
            "The potential applications and impacts are well-reasoned and insightful",
            "The response falls within the specified word count range (1000-1250 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

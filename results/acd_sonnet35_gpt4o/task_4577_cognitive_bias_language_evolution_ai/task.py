import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "Confirmation bias",
            "Availability heuristic",
            "Anchoring bias",
            "Dunning-Kruger effect"
        ]
        language_aspects = [
            "Vocabulary",
            "Syntax",
            "Pragmatics",
            "Semantics"
        ]
        return {
            "1": {
                "cognitive_bias": random.choice(cognitive_biases),
                "language_aspect": random.choice(language_aspects)
            },
            "2": {
                "cognitive_bias": random.choice(cognitive_biases),
                "language_aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the evolution of language while incorporating cognitive biases, then analyze its impact on communication efficiency and societal dynamics. Focus on the cognitive bias of {t['cognitive_bias']} and its influence on the language aspect of {t['language_aspect']}. Your response should include the following sections:\n\n1. AI System Design (300-350 words):\n   a) Describe the key components and architecture of your AI system.\n   b) Explain how your system models language evolution and incorporates cognitive biases.\n   c) Detail how {t['cognitive_bias']} is implemented and how it influences {t['language_aspect']}.\n   d) Discuss any novel algorithms or techniques used in your system.\n\n2. Simulation Parameters and Methodology (250-300 words):\n   a) Outline the parameters and variables used in your language evolution simulation.\n   b) Explain how you model the interaction between cognitive biases and language change.\n   c) Describe the timescale and population dynamics of your simulation.\n   d) Discuss how you ensure the simulation's validity and reliability.\n\n3. Analysis of Language Evolution (250-300 words):\n   a) Present the results of your simulation, focusing on how {t['cognitive_bias']} affects {t['language_aspect']}.\n   b) Analyze the patterns and trends observed in the simulated language evolution.\n   c) Compare your findings with real-world language evolution phenomena.\n   d) Discuss any unexpected or counterintuitive results from your simulation.\n\n4. Impact on Communication Efficiency (200-250 words):\n   a) Evaluate how the evolved language affects communication efficiency.\n   b) Discuss the trade-offs between cognitive biases and effective communication.\n   c) Propose metrics for measuring communication efficiency in your simulated language.\n\n5. Societal Implications (200-250 words):\n   a) Analyze potential societal impacts of the observed language evolution.\n   b) Discuss how cognitive biases in language might influence social structures and dynamics.\n   c) Consider the ethical implications of using AI to study and potentially influence language evolution.\n\n6. Future Research and Applications (150-200 words):\n   a) Suggest two potential extensions or improvements to your AI system.\n   b) Propose a research question that emerges from your findings.\n   c) Discuss potential real-world applications of your AI system and findings.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a word count at the end of your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the cognitive bias of {t['cognitive_bias']} and its influence on the language aspect of {t['language_aspect']}.",
            "The AI system design is innovative and scientifically plausible.",
            "The simulation methodology is well-described and appropriate for studying language evolution.",
            "The analysis of language evolution is thorough and insightful.",
            "The impact on communication efficiency is well-evaluated.",
            "The societal implications are thoughtfully considered.",
            "The proposed future research directions are relevant and interesting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            "Memory enhancement",
            "Sensory augmentation",
            "Emotional regulation",
            "Collective intelligence",
            "Accelerated learning"
        ]
        societal_aspects = [
            "Education and skill acquisition",
            "Workplace productivity and creativity",
            "Social interactions and relationships",
            "Healthcare and mental well-being",
            "Governance and decision-making"
        ]
        return {
            "1": {"cognitive_domain": random.choice(cognitive_domains), "societal_aspect": random.choice(societal_aspects)},
            "2": {"cognitive_domain": random.choice(cognitive_domains), "societal_aspect": random.choice(societal_aspects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a futuristic brain-computer interface (BCI) system that creates a symbiotic relationship between human cognition and artificial intelligence, focusing on the cognitive domain of {t['cognitive_domain']}. Then, analyze its potential impacts on {t['societal_aspect']}. Your response should include:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components and functioning of your proposed neuro-symbiotic interface.\n   b) Explain how it integrates with the human brain to enhance {t['cognitive_domain']}.\n   c) Detail the AI components and how they interact with human cognition.\n   d) Address potential challenges in implementing such a system and propose innovative solutions.\n\n2. Cognitive Enhancement Mechanism (250-300 words):\n   a) Explain the specific mechanisms by which your system enhances {t['cognitive_domain']}.\n   b) Describe how the symbiotic relationship between human and AI cognition functions in this domain.\n   c) Discuss potential limitations and how they might be addressed.\n\n3. Societal Impact Analysis (250-300 words):\n   a) Analyze how your neuro-symbiotic interface could impact {t['societal_aspect']}.\n   b) Discuss both potential benefits and risks to individuals and society.\n   c) Consider short-term and long-term consequences of widespread adoption.\n\n4. Ethical Considerations (200-250 words):\n   a) Identify key ethical issues raised by your neuro-symbiotic interface.\n   b) Propose guidelines or safeguards to address these ethical concerns.\n   c) Discuss how this technology might challenge or change our understanding of human identity and autonomy.\n\n5. Future Research Directions (150-200 words):\n   a) Suggest 2-3 key areas for further research to advance or better understand this technology.\n   b) Propose an experiment to test a critical aspect of your neuro-symbiotic interface.\n\n6. Interdisciplinary Implications (150-200 words):\n   a) Discuss how this technology might influence or be influenced by advances in other scientific fields.\n   b) Consider potential applications beyond {t['cognitive_domain']} and {t['societal_aspect']}.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and relevant social sciences. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor throughout your response.\n\nFormat your response with clear headings for each section, adhering to the word limits provided. Your total response should be between 1300-1600 words. Remember to consider ethical implications and maintain scientific plausibility in all aspects of your design and analysis."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, artificial intelligence, and their potential integration in enhancing {t['cognitive_domain']}.",
            "The proposed neuro-symbiotic interface is innovative, scientifically plausible, and clearly explained.",
            f"The analysis of societal impacts on {t['societal_aspect']} is comprehensive, considering both benefits and risks.",
            "The ethical considerations are thoughtfully explored, with proposed guidelines or safeguards.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving.",
            "The submission adheres to the specified format and word limits for each section.",
            "The proposed future research directions and experiments are relevant and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

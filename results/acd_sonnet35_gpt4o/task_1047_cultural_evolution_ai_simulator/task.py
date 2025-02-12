import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_domains = [
            "religion",
            "technology",
            "social norms",
            "art and aesthetics"
        ]
        transmission_mechanisms = [
            "vertical (parent to child)",
            "horizontal (peer to peer)",
            "oblique (elder to younger)",
            "media-based"
        ]
        environmental_factors = [
            "climate change",
            "technological disruption",
            "migration patterns",
            "economic shifts"
        ]
        return {
            "1": {
                "cultural_domain": random.choice(cultural_domains),
                "transmission_mechanism": random.choice(transmission_mechanisms),
                "environmental_factor": random.choice(environmental_factors)
            },
            "2": {
                "cultural_domain": random.choice(cultural_domains),
                "transmission_mechanism": random.choice(transmission_mechanisms),
                "environmental_factor": random.choice(environmental_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and simulates cultural evolution, focusing on the transmission and transformation of cultural memes across generations and societies. Your system should specifically address the cultural domain of {t['cultural_domain']}, the transmission mechanism of {t['transmission_mechanism']}, and the environmental factor of {t['environmental_factor']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for modeling cultural evolution.
   b) Explain how your system incorporates principles from cultural anthropology, cognitive science, and complex systems theory.
   c) Discuss how your system models individual agents, their interactions, and the emergence of collective behavior.
   d) Explain how your system handles the specific cultural domain, transmission mechanism, and environmental factor given in the prompt.

2. Meme Representation and Dynamics (200-250 words):
   a) Describe how cultural memes are represented in your system.
   b) Explain the mechanisms for meme transmission, mutation, and selection in your model.
   c) Discuss how your system accounts for the given transmission mechanism and its impact on meme propagation.
   d) Provide an example of how a specific meme might evolve in your system over time.

3. Environmental Interaction (200-250 words):
   a) Explain how your system models the impact of the given environmental factor on cultural evolution.
   b) Describe how environmental changes affect meme transmission and selection in your model.
   c) Discuss any feedback loops between cultural evolution and environmental changes in your system.

4. Simulation and Analysis (250-300 words):
   a) Describe how your system would run a simulation of cultural evolution over multiple generations.
   b) Explain the key parameters and variables in your simulation.
   c) Discuss the types of patterns or phenomena your system might reveal about cultural evolution.
   d) Propose a specific hypothesis about cultural evolution that your system could test, and describe how you would analyze the results.

5. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to model cultural evolution.
   b) Address any limitations or potential biases in your approach.
   c) Suggest safeguards or guidelines for the responsible use and interpretation of your system's outputs.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your AI system could contribute to our understanding of cultural anthropology and cognitive science.
   b) Propose a novel research question in cultural evolution that your system might help address.
   c) Suggest how insights from your system could be applied in fields such as sociology, marketing, or public policy.

Ensure your response demonstrates a deep understanding of cultural anthropology, cognitive science, and AI systems. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility. Your total response should be between 1200-1500 words.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Include a brief conclusion summarizing the key innovations and potential impact of your proposed AI system."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively models the cultural domain of {t['cultural_domain']}, the transmission mechanism of {t['transmission_mechanism']}, and the environmental factor of {t['environmental_factor']}",
            "The response demonstrates a deep understanding of cultural anthropology, cognitive science, and AI systems",
            "The proposed AI system is innovative and scientifically plausible",
            "The response addresses all required sections with appropriate depth and clarity",
            "The system architecture and meme dynamics are well-explained and theoretically grounded",
            "The simulation and analysis approach is well-designed and could yield meaningful insights",
            "Ethical considerations and limitations are thoughtfully discussed",
            "The interdisciplinary implications and potential applications are insightful and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

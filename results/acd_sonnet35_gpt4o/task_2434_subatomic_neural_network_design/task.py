import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        subatomic_particles = ['Quarks', 'Leptons', 'Bosons']
        environments = ['Neutron Star Interior', 'Black Hole Event Horizon', 'Supernova Core']
        applications = ['Extreme Computing', 'Cosmological Sensing', 'Quantum Gravity Probing']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'particle': random.choice(subatomic_particles),
                'environment': random.choice(environments),
                'application': random.choice(applications)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical neural network architecture using {t['particle']} for information processing in the extreme environment of a {t['environment']}, and analyze its potential applications in {t['application']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain how {t['particle']} could be used for information processing in a neural network.
   b) Describe the unique properties of the {t['environment']} that make it suitable for this architecture.
   c) Discuss how principles from particle physics and information theory inform your design.
   d) Cite at least two relevant scientific theories or principles that support your design.

2. Neural Network Architecture (300-350 words):
   a) Describe the key components of your subatomic neural network.
   b) Explain how information is encoded, processed, and transmitted in your network.
   c) Detail how your architecture adapts to the extreme conditions of the {t['environment']}.
   d) Provide a high-level diagram or pseudocode representing the network's structure and function. The diagram/pseudocode should include at least 3 layers and explain the interaction between {t['particle']} in each layer.

3. Information Processing Mechanisms (200-250 words):
   a) Explain the fundamental operations (e.g., activation functions, weight adjustments) in your subatomic neural network.
   b) Describe how your network handles error correction and noise reduction in the extreme environment.
   c) Compare the theoretical information processing capabilities of your network to conventional neural networks.

4. Potential Applications (200-250 words):
   a) Analyze how your subatomic neural network could be applied to {t['application']}.
   b) Discuss the potential advantages and limitations of your architecture for this application.
   c) Propose an experiment or simulation to test the feasibility of your network for the specified application.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your subatomic neural network for our understanding of computation and cognition.
   b) Explore potential technological or scientific advancements that could result from this architecture.
   c) Suggest areas for future research or improvements to your design.

Ensure your response demonstrates a deep understanding of particle physics, neural network principles, and the specified extreme environment. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words. Please include a word count at the end of your submission.

Note: Your response will be evaluated based on the depth of understanding demonstrated, the innovation and scientific plausibility of your design, the quality of your analysis of applications and implications, and the clarity and structure of your writing."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of particle physics, neural networks, and the specified extreme environment",
            "The proposed subatomic neural network architecture is innovative and scientifically plausible",
            "The response includes citations of at least two relevant scientific theories or principles",
            "The diagram or pseudocode includes at least 3 layers and explains the interaction between particles in each layer",
            "The potential applications and implications are well-analyzed and thought-provoking",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The submission includes a word count and falls within the specified range of 1200-1450 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

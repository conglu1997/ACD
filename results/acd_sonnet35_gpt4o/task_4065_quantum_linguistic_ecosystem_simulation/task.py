import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'Superposition',
                'linguistic_feature': 'Semantics',
                'ecosystem_type': 'Aquatic'
            },
            {
                'quantum_concept': 'Entanglement',
                'linguistic_feature': 'Syntax',
                'ecosystem_type': 'Terrestrial'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates an artificial ecosystem where organisms communicate and evolve using quantum linguistics. Your system should incorporate the quantum concept of {t['quantum_concept']}, focus on the linguistic feature of {t['linguistic_feature']}, and simulate a {t['ecosystem_type']} ecosystem. Then, analyze its implications for information theory and artificial life. Your response should include:

1. Quantum-Linguistic Framework (300-350 words):
   a) Explain how you integrate the specified quantum concept with the linguistic feature in your simulation.
   b) Describe the mathematical or conceptual model for quantum-linguistic communication in your ecosystem.
   c) Discuss how this framework captures both quantum behavior and language evolution.

2. Ecosystem Simulation Design (300-350 words):
   a) Outline the key components of your quantum computing system for simulating the artificial ecosystem.
   b) Explain how your system models organism communication, evolution, and interaction using quantum linguistics.
   c) Describe how the simulation incorporates the specified ecosystem type.
   d) Include a high-level diagram or pseudocode representing your simulation's architecture.

3. Quantum Computation Process (250-300 words):
   a) Detail how your quantum computing system processes and simulates quantum-linguistic interactions.
   b) Explain any novel quantum algorithms or operations you've developed for this simulation.
   c) Discuss how you address challenges in quantum coherence and error correction in your system.

4. Evolutionary Dynamics (200-250 words):
   a) Describe how organisms in your ecosystem evolve their quantum-linguistic capabilities over time.
   b) Explain how you model natural selection and adaptation in the context of quantum communication.
   c) Provide an example of how a specific trait or communication pattern might evolve in your simulation.

5. Information Theory Analysis (200-250 words):
   a) Analyze how quantum-linguistic communication in your ecosystem relates to classical information theory.
   b) Discuss any novel insights or principles of information processing that emerge from your simulation.
   c) Explain how these findings might contribute to our understanding of quantum information theory.

6. Artificial Life Implications (200-250 words):
   a) Explore how your quantum-linguistic ecosystem simulation could impact the field of artificial life.
   b) Discuss potential applications of your system in developing more advanced artificial life forms.
   c) Consider how this approach might lead to new paradigms in creating and understanding synthetic organisms.

7. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical concerns related to simulating quantum-linguistic life forms.
   b) Propose guidelines for responsible development and use of such simulations.
   c) Suggest two future research directions that could extend or refine your approach.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, ecology, information theory, and artificial life. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response integrates the quantum concept of {t['quantum_concept']} with the linguistic feature of {t['linguistic_feature']} in a coherent framework.",
            f"The ecosystem simulation design incorporates a {t['ecosystem_type']} ecosystem and uses quantum linguistics for organism communication and evolution.",
            "The quantum computation process is explained in detail, including novel algorithms or operations.",
            "The evolutionary dynamics of quantum-linguistic capabilities are described with a specific example.",
            "The information theory analysis provides novel insights related to quantum-linguistic communication.",
            "The artificial life implications are explored, including potential applications and new paradigms.",
            "Ethical considerations are addressed, and future research directions are proposed.",
            "The response demonstrates a deep understanding of quantum computing, linguistics, ecology, information theory, and artificial life.",
            "The ideas presented are creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

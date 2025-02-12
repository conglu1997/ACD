import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Quantum entanglement",
                "neural_mechanism": "Synaptic plasticity",
                "ecosystem_focus": "Coral reef symbiosis",
                "environmental_challenge": "Ocean acidification"
            },
            {
                "quantum_principle": "Quantum superposition",
                "neural_mechanism": "Neural oscillations",
                "ecosystem_focus": "Soil microbiome networks",
                "environmental_challenge": "Sustainable agriculture"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-neural interface system for monitoring and influencing ecosystem dynamics, then analyze its potential applications and ethical implications. Your system should incorporate the quantum principle of {t['quantum_principle']}, the neural mechanism of {t['neural_mechanism']}, and focus on the ecosystem aspect of {t['ecosystem_focus']}. Apply your system to address the environmental challenge of {t['environmental_challenge']}.

Your response should include the following sections:

1. System Design (300-350 words):
   a) Describe the key components and functionality of your quantum-neural interface system.
   b) Explain how it incorporates {t['quantum_principle']} and {t['neural_mechanism']}.
   c) Detail how the system interacts with and monitors {t['ecosystem_focus']}.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Quantum-Neural Integration (250-300 words):
   a) Explain how quantum principles are translated into neural processes in your system.
   b) Discuss potential challenges in integrating quantum and neural components.
   c) Propose a novel mechanism for quantum-neural information processing.

3. Ecosystem Interaction (250-300 words):
   a) Describe how your system monitors and influences {t['ecosystem_focus']}.
   b) Explain the potential benefits of using a quantum-neural approach for ecosystem management.
   c) Discuss any potential risks or unintended consequences of your system's interaction with the ecosystem.

4. Application to Environmental Challenge (200-250 words):
   a) Outline how your system could be applied to address {t['environmental_challenge']}.
   b) Provide a hypothetical scenario demonstrating the system's effectiveness.
   c) Discuss potential limitations of your approach.

5. Ethical Implications (200-250 words):
   a) Identify three major ethical concerns raised by your quantum-neural ecosystem interface.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, biocentrism).
   c) Propose guidelines for the responsible development and use of such systems.

6. Future Directions and Societal Impact (150-200 words):
   a) Speculate on potential future advancements or extensions of your system.
   b) Discuss how these developments might impact society and our relationship with ecosystems.
   c) Propose a related area of research that could enhance quantum-neural-ecological interfaces.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and ecology. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and ecology",
            "The system design is innovative, well-explained, and incorporates the specified quantum principle and neural mechanism",
            "The quantum-neural integration is plausibly described and addresses potential challenges",
            "The ecosystem interaction is well-thought-out and considers both benefits and risks",
            f"The application to {t['environmental_challenge']} is clearly explained and includes a plausible scenario",
            "The ethical implications are thoroughly analyzed using an appropriate ethical framework",
            "The response is well-formatted with clear headings and falls within the specified word count range (1350-1650 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

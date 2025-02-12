import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum entanglement",
            "quantum superposition",
            "quantum tunneling"
        ]
        neural_mechanisms = [
            "synaptic plasticity",
            "neural oscillations",
            "neuromodulation"
        ]
        information_concepts = [
            "error correction",
            "data compression",
            "channel capacity"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_mechanism": random.choice(neural_mechanisms),
                "information_concept": random.choice(information_concepts)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neural_mechanism": random.choice(neural_mechanisms),
                "information_concept": random.choice(information_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical communication system that integrates principles from quantum mechanics, neuroscience, and information theory to enable faster-than-light information transfer between two conscious entities. Your system should specifically incorporate {t['quantum_principle']}, {t['neural_mechanism']}, and {t['information_concept']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum neural communication system.
   b) Explain how {t['quantum_principle']}, {t['neural_mechanism']}, and {t['information_concept']} are integrated into the system design.
   c) Provide a high-level diagram or detailed description of your system's architecture.
   d) Discuss how your system achieves faster-than-light information transfer while addressing potential conflicts with current understanding of physics.

2. Quantum-Neural Interface (250-300 words):
   a) Explain how your system interfaces quantum processes with neural mechanisms.
   b) Describe the theoretical basis for this interface, drawing on relevant research in quantum biology or quantum cognition.
   c) Discuss how {t['neural_mechanism']} is enhanced or modified by quantum effects in your system.

3. Information Processing and Transfer (250-300 words):
   a) Detail how information is encoded, processed, and transferred in your system.
   b) Explain how {t['information_concept']} is implemented in the quantum-neural context.
   c) Analyze the theoretical information transfer rate and efficiency of your system.

4. Consciousness and Perception (200-250 words):
   a) Discuss how your system interfaces with conscious perception in the communicating entities.
   b) Explain any potential effects on subjective experience or mental states during the communication process.
   c) Address ethical considerations related to faster-than-light information transfer between conscious entities.

5. Theoretical Challenges and Limitations (200-250 words):
   a) Identify key theoretical challenges or potential contradictions in your proposed system.
   b) Discuss how these challenges might be addressed or resolved.
   c) Analyze the limitations of your system and propose areas for further theoretical development.

6. Experimental Proposal (150-200 words):
   a) Propose a theoretical experiment or observation that could provide evidence for the feasibility of your system.
   b) Describe the expected results and how they would support your proposed mechanism.
   c) Discuss any technological or methodological barriers to conducting such an experiment.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates {t['quantum_principle']}, {t['neural_mechanism']}, and {t['information_concept']} into the system design",
            "The proposed system demonstrates a deep understanding of quantum mechanics, neuroscience, and information theory",
            "The response addresses the challenge of faster-than-light information transfer in a scientifically plausible manner",
            "The system architecture and quantum-neural interface are well-described and logically consistent",
            "The response includes creative and speculative elements while maintaining overall scientific plausibility",
            "Theoretical challenges and limitations are thoughtfully addressed",
            "The proposed experimental design is relevant and well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

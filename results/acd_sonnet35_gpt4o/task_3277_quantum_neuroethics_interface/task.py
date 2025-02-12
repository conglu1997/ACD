import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence"
        ]
        brain_regions = [
            "Prefrontal cortex",
            "Hippocampus",
            "Amygdala",
            "Cerebellum"
        ]
        cognitive_enhancements = [
            "Memory augmentation",
            "Accelerated learning",
            "Enhanced problem-solving",
            "Improved emotional regulation"
        ]
        ethical_dilemmas = [
            "Privacy and mental autonomy",
            "Cognitive inequality",
            "Authenticity of enhanced cognition",
            "Long-term effects on human evolution"
        ]
        tasks = [
            {
                "quantum_phenomenon": qp,
                "brain_region": br,
                "cognitive_enhancement": ce,
                "ethical_dilemma": ed
            }
            for qp in quantum_phenomena
            for br in brain_regions
            for ce in cognitive_enhancements
            for ed in ethical_dilemmas
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-neural interface system that connects human brains to quantum computers, focusing on the quantum phenomenon of {t['quantum_phenomenon']} and targeting the {t['brain_region']}. Then, analyze its implications for {t['cognitive_enhancement']} and the ethical dilemma of {t['ethical_dilemma']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-neural interface system.
   b) Explain how it leverages {t['quantum_phenomenon']} to interface with the {t['brain_region']}.
   c) Discuss any novel technologies or approaches used in your design.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Quantum-Neural Integration (250-300 words):
   a) Explain how your system translates between quantum states and neural activity.
   b) Discuss potential challenges in maintaining quantum coherence in a biological environment.
   c) Propose a method for validating the fidelity of the quantum-neural information transfer.

3. Cognitive Enhancement Analysis (200-250 words):
   a) Describe how your system could potentially achieve {t['cognitive_enhancement']}.
   b) Analyze the possible mechanisms and limitations of this enhancement.
   c) Discuss how this enhancement might impact human cognition and behavior.

4. Ethical Implications (250-300 words):
   a) Analyze the ethical dilemma of {t['ethical_dilemma']} in the context of your quantum-neural interface.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines or policies to address the identified ethical issues.

5. Future Research Directions (150-200 words):
   a) Suggest two potential advancements or extensions of your quantum-neural interface system.
   b) Discuss how these developments might impact our understanding of consciousness or cognition.
   c) Propose a related area of research that could enhance quantum-neural interfaces.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and ethics. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains how {t['quantum_phenomenon']} is leveraged in the quantum-neural interface system",
            f"The system design effectively targets and interfaces with the {t['brain_region']}",
            f"The cognitive enhancement of {t['cognitive_enhancement']} is thoroughly analyzed and explained",
            f"The ethical implications of {t['ethical_dilemma']} are comprehensively discussed in the context of the quantum-neural interface",
            "The response demonstrates a deep understanding of quantum physics, neuroscience, and ethics",
            "The proposed system and analysis are innovative while maintaining scientific plausibility",
            "The response addresses all required sections and is within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

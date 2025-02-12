import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                'effect': 'Quantum entanglement',
                'brain_region': 'Hippocampus',
                'conscious_experience': 'Memory formation and recall'
            },
            {
                'effect': 'Quantum superposition',
                'brain_region': 'Prefrontal cortex',
                'conscious_experience': 'Decision-making and planning'
            },
            {
                'effect': 'Quantum tunneling',
                'brain_region': 'Visual cortex',
                'conscious_experience': 'Visual perception and processing'
            },
            {
                'effect': 'Quantum coherence',
                'brain_region': 'Thalamus',
                'conscious_experience': 'Sensory integration and awareness'
            }
        ]
        return {str(i+1): effect for i, effect in enumerate(random.sample(quantum_effects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-based brain-computer interface that could potentially access and manipulate conscious experiences, focusing on the quantum effect of {t['effect']} in the {t['brain_region']} to influence {t['conscious_experience']}. Then, analyze its implications for our understanding of consciousness and reality. Your response should include:

0. Key Concepts (100-150 words):
   Briefly explain the key concepts of {t['effect']}, the function of the {t['brain_region']}, and the nature of {t['conscious_experience']}.

1. Quantum-Neural Interface Design (300-350 words):
   a) Describe the key components and functioning of your proposed interface.
   b) Explain how it leverages {t['effect']} to interact with neural activity in the {t['brain_region']}.
   c) Discuss the theoretical basis for how this interaction could influence {t['conscious_experience']}.
   d) Address potential challenges in maintaining quantum effects in the brain and propose solutions.

2. Experimental Protocol (250-300 words):
   a) Outline a hypothetical experiment to test your interface's ability to access or manipulate {t['conscious_experience']}.
   b) Describe the experimental setup, including any novel equipment or techniques.
   c) Explain how you would measure and verify the interface's effects on consciousness.
   d) Discuss potential confounding factors and how you would control for them.

3. Implications for Consciousness Theory (200-250 words):
   a) Analyze how your interface's functioning might inform or challenge current theories of consciousness.
   b) Discuss the implications of quantum effects in neural processing for the nature of subjective experience.
   c) Consider how the ability to manipulate consciousness through quantum means might affect our understanding of free will and determinism.

4. Philosophical and Ethical Considerations (200-250 words):
   a) Explore the philosophical implications of a quantum basis for consciousness.
   b) Discuss ethical concerns related to accessing and manipulating conscious experiences.
   c) Consider potential societal impacts if such technology were to be developed.
   d) Propose ethical guidelines for research and potential applications of quantum consciousness interfaces.

5. Future Research Directions (150-200 words):
   a) Suggest 2-3 follow-up research questions or experiments based on your proposal.
   b) Discuss how advances in this field might influence other areas of science and technology.
   c) Speculate on potential long-term implications for our understanding of reality and the nature of mind.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section (0. Key Concepts, 1. Quantum-Neural Interface Design, etc.). Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of key concepts related to {t['effect']}, the {t['brain_region']}, and {t['conscious_experience']}.",
            f"The quantum-neural interface design demonstrates a creative and scientifically grounded application of {t['effect']} to influence {t['conscious_experience']}.",
            "The experimental protocol is well-designed, addressing potential challenges and confounding factors.",
            "The analysis of implications for consciousness theory is insightful and considers multiple perspectives.",
            "The discussion of philosophical and ethical considerations is thorough and thought-provoking.",
            "The proposed future research directions are innovative and build upon the presented ideas.",
            "The response effectively integrates concepts from quantum physics, neuroscience, and philosophy of mind.",
            "The writing is clear, well-structured, and adheres to the specified format and word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

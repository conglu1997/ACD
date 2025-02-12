import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "brain_state": "Relaxed meditation",
                "musical_style": "Ambient",
                "quantum_concept": "Superposition"
            },
            {
                "brain_state": "Focused problem-solving",
                "musical_style": "Classical",
                "quantum_concept": "Entanglement"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that analyzes brain activity patterns associated with {t['brain_state']} and translates them into {t['musical_style']} musical compositions. Your system should incorporate the quantum mechanical concept of {t['quantum_concept']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum neural music synthesis system.
   b) Explain how your system integrates neuroscience, quantum computing, and music theory.
   c) Detail how you've incorporated the {t['quantum_concept']} concept into your system's design.
   d) Discuss how your system processes brain activity data and translates it into musical elements.

2. Quantum-Neural Interface (250-300 words):
   a) Explain how your system quantum-mechanically represents neural activity patterns.
   b) Describe how the {t['quantum_concept']} concept is used to process or transform this neural data.
   c) Discuss any novel quantum algorithms or operations you've developed for this purpose.

3. Music Generation Process (250-300 words):
   a) Detail how your system translates quantum-processed neural data into musical elements (e.g., melody, harmony, rhythm).
   b) Explain how your system ensures the generated music adheres to the principles of {t['musical_style']} style.
   c) Describe any machine learning or AI components involved in the music generation process.

4. Neuroscientific Basis (200-250 words):
   a) Discuss the neuroscientific principles underlying your system's interpretation of {t['brain_state']}.
   b) Explain how your system accounts for individual differences in brain activity patterns.
   c) Describe how your system might adapt to changes in the user's brain state over time.

5. Potential Applications and Implications (150-200 words):
   a) Propose two potential applications of your quantum neural music synthesis system outside of artistic creation.
   b) Discuss the implications of your system for our understanding of consciousness, creativity, and the relationship between brain activity and music.
   c) Suggest how this technology could be used in therapeutic or scientific contexts.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues related to using this technology.
   b) Discuss any limitations of your approach and potential biases in the system.
   c) Propose guidelines for responsible development and use of quantum neural music synthesis technology.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the translation of brain activity patterns associated with {t['brain_state']} into {t['musical_style']} musical compositions.",
            f"The proposed system must incorporate the quantum concept of {t['quantum_concept']} in a meaningful and scientifically plausible way.",
            "The system design must integrate principles from quantum computing, neuroscience, and music theory, demonstrating a clear understanding of each field.",
            "The submission must include all six required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The proposed quantum neural music synthesis system must be logically coherent and demonstrate a clear understanding of how the interdisciplinary concepts work together.",
            "The response must be creative and propose novel ideas while remaining grounded in scientific principles from the relevant fields.",
            f"The explanation of how {t['quantum_concept']} is used in the system must be scientifically plausible and well-reasoned.",
            "The ethical considerations and limitations discussion must be thoughtful and demonstrate an understanding of the broader implications of the proposed technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

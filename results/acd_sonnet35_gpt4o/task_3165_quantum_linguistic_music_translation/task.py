import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_states = [
            "Two-qubit density matrix with partial entanglement",
            "Three-qubit cluster state",
            "Four-qubit graph state",
            "Quantum error correcting code state"
        ]
        linguistic_structures = [
            "Combinatory categorial grammar",
            "Head-driven phrase structure grammar",
            "Lexical functional grammar",
            "Optimality theory constraints"
        ]
        musical_elements = [
            "Harmonic progression",
            "Polyrhythmic structure",
            "Melodic contour",
            "Spectral composition"
        ]
        return {
            "1": {
                "quantum_state": random.choice(quantum_states),
                "linguistic_structure": random.choice(linguistic_structures),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "quantum_state": random.choice(quantum_states),
                "linguistic_structure": random.choice(linguistic_structures),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates quantum states into musical notation using linguistic structures as an intermediary. Focus on the quantum state of {t['quantum_state']}, using {t['linguistic_structure']} as the linguistic intermediary, and {t['musical_element']} as the primary musical element to be generated. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-linguistic-music translation system.
   b) Explain how quantum information is mapped onto linguistic structures.
   c) Detail the process of converting linguistic representations into musical notation.
   d) Discuss any novel algorithms or techniques used in your system.
   e) Provide a visual representation or diagram of your system architecture.
   f) Include a small code snippet (10-15 lines) demonstrating a key aspect of your system.

2. Quantum-Linguistic Mapping (300-350 words):
   a) Explain how the specified quantum state is represented using the given linguistic structure.
   b) Discuss the challenges in preserving quantum information during this mapping.
   c) Provide a specific example of how a quantum property is encoded linguistically.
   d) Include a mathematical formulation of your quantum-linguistic mapping process.

3. Linguistic-Musical Translation (250-300 words):
   a) Describe how the linguistic representation is transformed into the specified musical element.
   b) Explain how your system ensures musical coherence and aesthetic quality.
   c) Discuss how quantum properties might influence musical characteristics.
   d) Provide a specific example of how a musical element could encode quantum information.

4. Sample Output Analysis (200-250 words):
   a) Provide a detailed description of a musical piece your system might generate.
   b) Analyze how specific aspects of the quantum state and linguistic structure are reflected in the music.
   c) Discuss the potential artistic and scientific value of this generated piece.

5. Implications and Applications (200-250 words):
   a) Explore potential applications of your system in quantum information theory.
   b) Discuss how this approach might inform new compositional techniques in music.
   c) Speculate on the implications for our understanding of the relationships between quantum physics, language, and music.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in your approach.
   b) Propose future research directions or extensions of your system.
   c) Suggest an experiment to validate the quantum-linguistic-musical relationships proposed by your system.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, linguistics, and music theory.",
            "The system architecture is well-designed and clearly explained, showing how quantum states are mapped to linguistic structures and then to musical elements.",
            "The quantum-linguistic mapping and linguistic-musical translation processes are logically sound and creative.",
            "The sample output analysis provides a clear connection between the quantum state, linguistic structure, and musical element specified in the task.",
            "The implications and applications discussed are insightful and demonstrate interdisciplinary thinking.",
            "The limitations and future directions show critical thinking and propose valid research questions.",
            "The overall response is innovative while maintaining scientific plausibility.",
            "The response falls within the specified word count range of 1450-1750 words.",
            "The mathematical formulation of the quantum-linguistic mapping is provided and is coherent.",
            "A visual representation or diagram of the system architecture is included and is clear and informative.",
            "The code snippet demonstrates a key aspect of the system and is relevant to the task.",
            "A specific example of how a musical element could encode quantum information is provided and is plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

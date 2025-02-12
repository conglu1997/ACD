import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "neural_mechanism": "Synaptic plasticity",
                "music_genre": "Jazz"
            },
            {
                "quantum_principle": "Entanglement",
                "neural_mechanism": "Neuronal oscillations",
                "music_genre": "Classical"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network system for composing music that incorporates principles from neuroscience and quantum mechanics. Focus on the quantum principle of {t['quantum_principle']}, the neural mechanism of {t['neural_mechanism']}, and apply it to composing {t['music_genre']} music. Your response should include:

1. Quantum-Neural Architecture (300-350 words):
   a) Describe the key components of your quantum-inspired neural network for music composition.
   b) Explain how you incorporate the specified quantum principle into the network architecture.
   c) Detail how the neural mechanism is integrated into the system.
   d) Discuss how this architecture specifically supports {t['music_genre']} composition.
   e) Include a high-level diagram or pseudocode snippet illustrating a key aspect of your system.

2. Quantum-Neural Processes (250-300 words):
   a) Explain how your system uses {t['quantum_principle']} in the process of music composition.
   b) Describe how the {t['neural_mechanism']} influences the generation of musical elements.
   c) Discuss any novel computational advantages this quantum-neural approach might offer over classical systems.

3. Music Composition Methodology (250-300 words):
   a) Outline the step-by-step process your system uses to compose {t['music_genre']} music.
   b) Explain how quantum and neural principles interact to generate musical structures (e.g., melody, harmony, rhythm).
   c) Describe how your system ensures the composed music adheres to {t['music_genre']} conventions while maintaining creativity.

4. Theoretical Foundations (200-250 words):
   a) Provide the theoretical basis for combining quantum mechanics, neuroscience, and music theory in your system.
   b) Discuss any existing research or theories that support your approach.
   c) Address potential criticisms or limitations of applying quantum principles to neural networks and music composition.

5. Practical Implementation and Challenges (200-250 words):
   a) Describe the computational requirements for implementing your system.
   b) Discuss any technical challenges in realizing this quantum-neural music composer.
   c) Propose solutions or workarounds for these challenges.

6. Artistic and Scientific Implications (200-250 words):
   a) Analyze the potential impact of your system on music composition and performance.
   b) Discuss how this approach might influence our understanding of creativity and consciousness.
   c) Explore possible applications of your system beyond music composition.

7. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to using quantum-neural AI for creative tasks.
   b) Discuss the implications for human musicians and composers.
   c) Propose guidelines for the responsible development and use of such systems in the arts.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified quantum principle, neural mechanism, and music genre.",
            "The quantum-neural architecture is well-designed and clearly explained, with innovative integration of quantum and neural concepts.",
            "The music composition methodology is logically presented and effectively combines quantum, neural, and musical elements.",
            "The theoretical foundations are sound and well-argued, with appropriate references to existing research.",
            "Practical implementation challenges are realistically addressed with feasible solutions proposed.",
            "The artistic and scientific implications are thoughtfully explored, demonstrating creativity and foresight.",
            "Ethical considerations are thoroughly discussed with responsible guidelines proposed.",
            "The response shows exceptional creativity and interdisciplinary knowledge integration throughout.",
            "The submission adheres to the specified word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

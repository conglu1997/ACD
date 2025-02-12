import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            "syntax trees",
            "phonological rules",
            "semantic networks",
            "discourse structures"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum Fourier transform",
            "quantum annealing"
        ]
        
        return {
            "1": {
                "linguistic_structure": random.choice(linguistic_structures),
                "musical_element": random.choice(musical_elements),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "linguistic_structure": random.choice(linguistic_structures),
                "musical_element": random.choice(musical_elements),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm that composes music based on linguistic structures. Your algorithm should use {t['linguistic_structure']} to generate {t['musical_element']}, incorporating the quantum principle of {t['quantum_principle']}. Then, analyze its potential applications in cognitive science and musicology. Your response should include:

1. Quantum Algorithm Design (250-300 words):
   a) Describe the overall structure of your quantum algorithm for music composition.
   b) Explain how it incorporates the specified linguistic structure and musical element.
   c) Detail how the quantum principle is utilized in the composition process.
   d) Provide a high-level pseudocode or flow diagram of your algorithm.

2. Linguistic-Musical Mapping (200-250 words):
   a) Explain how your algorithm translates the linguistic structure into musical elements.
   b) Describe any challenges in this mapping and how you address them.
   c) Discuss how the quantum principle enhances this translation process.

3. Composition Process (200-250 words):
   a) Walk through a step-by-step example of how your algorithm would compose a short musical phrase.
   b) Explain how the quantum and classical parts of your algorithm interact during this process.
   c) Discuss any unique features or capabilities of your quantum approach compared to classical algorithms.

4. Cognitive Science Applications (150-200 words):
   a) Propose how your algorithm could be used to study the relationship between language and music processing in the brain.
   b) Discuss potential insights this approach might offer into cognitive processes underlying creativity.
   c) Suggest an experiment to test a hypothesis about language-music connections using your algorithm.

5. Musicological Implications (150-200 words):
   a) Analyze how your quantum linguistic-musical algorithm might influence music theory or composition techniques.
   b) Discuss potential applications in music analysis or generative music systems.
   c) Explore how this approach might bridge gaps between linguistic and musical studies.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic structures, and music theory. Be innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly describe a quantum algorithm that uses {t['linguistic_structure']} to generate {t['musical_element']}, incorporating the quantum principle of {t['quantum_principle']}.",
            "The algorithm design should be scientifically plausible and well-explained, demonstrating a deep understanding of quantum computing, linguistics, and music theory.",
            "The linguistic-musical mapping and composition process should be logically described and creatively approached.",
            "The response should provide thoughtful and innovative applications in cognitive science and musicology.",
            "The explanation should use appropriate technical terminology from quantum computing, linguistics, and music theory, with clear explanations of complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

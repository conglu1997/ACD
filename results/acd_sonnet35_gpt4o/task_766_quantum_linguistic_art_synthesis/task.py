import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_structures = [
            {
                'structure': 'Syntax trees',
                'art_style': 'Abstract expressionism',
                'quantum_principle': 'Superposition'
            },
            {
                'structure': 'Phonological rules',
                'art_style': 'Cubism',
                'quantum_principle': 'Entanglement'
            }
        ]
        return {str(i+1): structure for i, structure in enumerate(linguistic_structures)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that translates linguistic structures into visual art representations, incorporating principles of quantum computing. Your task has the following parameters:

Linguistic Structure: {t['structure']}
Art Style: {t['art_style']}
Quantum Principle: {t['quantum_principle']}

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum computing system for linguistic-to-visual translation.
   b) Explain how it incorporates the specified quantum principle in its design.
   c) Detail how the system will capture and represent the given linguistic structure.
   d) Discuss how the system will generate output in the specified art style.

2. Quantum-Linguistic-Visual Interface (200-250 words):
   a) Explain how your system translates linguistic data into quantum states.
   b) Describe how these quantum states are then transformed into visual representations.
   c) Discuss any challenges in mapping between these three domains (linguistic, quantum, and visual) and how you address them.

3. Artistic Generation Algorithm (200-250 words):
   a) Propose a quantum algorithm for generating visual art based on linguistic input.
   b) Explain how this algorithm leverages the specified quantum principle.
   c) Describe how the algorithm ensures the output adheres to the given art style.

4. Example Output (150-200 words):
   a) Provide a detailed description of a potential visual output from your system, based on a specific linguistic input of your choice.
   b) Explain how this output reflects the linguistic structure, quantum principle, and art style.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of language, quantum phenomena, and artistic creation.
   b) Propose two novel applications of your quantum linguistic-visual synthesis system outside of pure artistic creation.
   c) Speculate on how this technology might impact fields such as cognitive science, art therapy, or data visualization.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic structures, and art theory. Be innovative in your approach while maintaining scientific and artistic plausibility. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, and the specified art style",
            "The system architecture effectively incorporates the given quantum principle",
            "The quantum-linguistic-visual interface is clearly explained and plausible",
            "The artistic generation algorithm is innovative and leverages quantum principles",
            "The example output description is detailed and reflects all required elements",
            "The implications and applications are thoughtful and demonstrate interdisciplinary thinking",
            "The response is creative while maintaining scientific and artistic plausibility",
            "The response adheres to the specified word limit (1000-1250 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

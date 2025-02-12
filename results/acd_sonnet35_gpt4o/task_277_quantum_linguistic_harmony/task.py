import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_concept': 'Superposition',
                'linguistic_structure': 'Syntactic ambiguity'
            },
            {
                'quantum_concept': 'Entanglement',
                'linguistic_structure': 'Semantic relationships'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a musical system that integrates the quantum computing concept of {t['quantum_concept']} with the linguistic structure of {t['linguistic_structure']}. Then, compose and analyze a short piece using this system. Your task has the following parts:

1. Quantum-Linguistic Musical System Design (200-250 words):
   a) Explain how you will apply {t['quantum_concept']} to musical elements (e.g., pitch, rhythm, harmony).
   b) Describe how you will incorporate {t['linguistic_structure']} into your musical system.
   c) Outline the key components and rules of your system, including how it differs from traditional music theory.

2. Composition (150-200 words):
   a) Compose a short musical piece (or section of a piece) using your quantum-linguistic system.
   b) Provide a notated representation of your composition (use ASCII or Unicode characters if needed).
   c) Explain how your composition demonstrates the principles of your system, highlighting both quantum and linguistic aspects.

3. Analysis (200-250 words):
   a) Analyze the potential cognitive or perceptual effects of music created with your system.
   b) Compare these effects with those typically associated with traditional Western music.
   c) Discuss any challenges or unique opportunities in composing or performing music with this system.

4. Quantum-Linguistic-Musical Connections (150-200 words):
   a) Explain how your musical system might relate to or inspire developments in quantum computing or linguistics.
   b) Propose an experiment or study that could explore the cognitive or computational implications of your quantum-linguistic music system.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic structures, and music theory, while showcasing creativity in system design and composition. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The explanation of how {t['quantum_concept']} is applied to musical elements is clear and innovative.",
            f"The incorporation of {t['linguistic_structure']} into the musical system is well-explained and logical.",
            "The musical system design demonstrates a deep understanding of quantum computing, linguistics, and music theory.",
            "The composition effectively demonstrates the principles of the quantum-linguistic musical system.",
            "The analysis of cognitive or perceptual effects is insightful and well-reasoned.",
            "The proposed experiment or study is creative and scientifically sound.",
            "The overall response shows originality, interdisciplinary thinking, and a balance of creativity with scientific/musical plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

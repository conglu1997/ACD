import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_phenomena = [
            "DNA replication",
            "Protein folding",
            "Neural signal propagation",
            "Photosynthesis",
            "Cellular respiration"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum coherence",
            "Quantum measurement"
        ]
        return {
            "1": {
                "biological_phenomenon": random.choice(biological_phenomena),
                "quantum_concept": random.choice(quantum_concepts)
            },
            "2": {
                "biological_phenomenon": random.choice(biological_phenomena),
                "quantum_concept": random.choice(quantum_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired system for modeling and manipulating biological information processing, then apply it to {t['biological_phenomenon']}, focusing on the quantum concept of {t['quantum_concept']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired bioinformation system.
   b) Explain how it incorporates principles from quantum physics, biology, and information theory.
   c) Detail any novel quantum-inspired algorithms or techniques used in your design.
   d) Include a brief diagram or flowchart description representing your system architecture.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system models the specified biological phenomenon using quantum-inspired principles.
   b) Describe how the quantum concept of {t['quantum_concept']} is applied in your model.
   c) Discuss the advantages of your quantum-inspired approach over classical modeling techniques.

3. Information Processing and Manipulation (200-250 words):
   a) Detail how your system processes and manipulates biological information.
   b) Provide an example of how it could be used to analyze or predict aspects of {t['biological_phenomenon']}.
   c) Explain any potential for enhancing or modifying the biological process through your system.

4. Theoretical Implications (150-200 words):
   a) Discuss how your system might inform our understanding of the role of quantum effects in biological systems.
   b) Speculate on potential fundamental connections between quantum physics and biology suggested by your model.

5. Practical Applications (150-200 words):
   a) Propose two potential real-world applications of your quantum-inspired bioinformation system.
   b) Explain how these applications could advance research or technology in biology, medicine, or bioengineering.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your system.
   b) Suggest areas for future research or technological development to overcome these limitations.
   c) Propose an experiment to validate your system's predictions or capabilities.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, biology, and information theory.",
            "The system architecture is clearly described and incorporates principles from all three fields.",
            f"The quantum concept of {t['quantum_concept']} is effectively applied to model {t['biological_phenomenon']}.",
            "The response includes innovative ideas while maintaining scientific plausibility.",
            "Practical applications and theoretical implications are thoughtfully discussed.",
            "Limitations and future research directions are identified and addressed.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

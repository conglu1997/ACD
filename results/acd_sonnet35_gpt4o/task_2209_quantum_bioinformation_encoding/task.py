import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_structure': 'Protein',
                'quantum_property': 'Superposition',
                'information_aspect': 'Folding patterns'
            },
            {
                'biological_structure': 'Cell membrane',
                'quantum_property': 'Entanglement',
                'information_aspect': 'Signaling pathways'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based system for encoding and transmitting complex biological information about {t['biological_structure']}s, inspired by DNA storage mechanisms and quantum information theory. Your system should utilize the quantum property of {t['quantum_property']} and focus on encoding {t['information_aspect']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum bioinformation encoding system.
   b) Explain how your system leverages {t['quantum_property']} for information encoding.
   c) Detail how biological information about {t['information_aspect']} is represented in your quantum system.

2. Encoding Mechanism (200-250 words):
   a) Explain the process of encoding biological information into quantum states.
   b) Describe how your system achieves high information density.
   c) Discuss any error correction or redundancy mechanisms in your encoding scheme.

3. Information Retrieval and Decoding (200-250 words):
   a) Outline the process of retrieving and decoding the quantum-encoded biological information.
   b) Explain how the original {t['information_aspect']} can be accurately reconstructed.
   c) Discuss any potential sources of error in the decoding process and how they are mitigated.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum bioinformation encoding system to traditional biological information storage (e.g., DNA).
   b) Discuss potential advantages and limitations of your approach.
   c) Explain how your system might provide insights into the role of quantum effects in biological systems.

5. Potential Applications (150-200 words):
   a) Propose two potential applications of your quantum bioinformation encoding system in fields such as medicine, biotechnology, or synthetic biology.
   b) Explain how these applications could advance our understanding or manipulation of biological systems.

6. Ethical Considerations and Future Directions (100-150 words):
   a) Discuss potential ethical implications of using quantum systems to encode and manipulate biological information.
   b) Suggest future research directions to further develop and validate your proposed system.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and information theory. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1350 words. Begin each section with the heading (e.g., '1. System Architecture') on a new line, followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the quantum property of {t['quantum_property']} in the context of encoding biological information.",
            f"The system design focuses on encoding {t['information_aspect']} of {t['biological_structure']}s.",
            "The proposed system demonstrates a deep understanding of quantum physics, biology, and information theory.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            "All sections (System Architecture, Encoding Mechanism, Information Retrieval and Decoding, Comparative Analysis, Potential Applications, and Ethical Considerations and Future Directions) are adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

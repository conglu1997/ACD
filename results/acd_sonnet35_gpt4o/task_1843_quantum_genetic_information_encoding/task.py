import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            {
                "property": "superposition",
                "description": "The ability of a quantum system to exist in multiple states simultaneously"
            },
            {
                "property": "entanglement",
                "description": "A quantum phenomenon where particles become correlated and share properties regardless of distance"
            }
        ]
        genetic_elements = [
            {
                "element": "nucleotides",
                "description": "The building blocks of DNA and RNA (A, T, C, G, and U)"
            },
            {
                "element": "codons",
                "description": "Three-nucleotide sequences that code for specific amino acids"
            }
        ]
        return {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "genetic_element": random.choice(genetic_elements)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "genetic_element": random.choice(genetic_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system for encoding genetic information using quantum states, focusing on the quantum property of {t['quantum_property']['property']} and the genetic element of {t['genetic_element']['element']}. Analyze the potential implications of this system for genetic engineering and information storage. Your response should include:

1. Quantum-Genetic Encoding System (300-350 words):
   a) Describe your proposed system for encoding {t['genetic_element']['element']} using quantum states.
   b) Explain how you utilize the quantum property of {t['quantum_property']['property']} in your encoding scheme.
   c) Provide a specific example of how a genetic sequence would be encoded in your system.
   d) Discuss any advantages your system might have over classical genetic encoding.

2. Theoretical Framework (250-300 words):
   a) Outline the key principles from quantum physics and genetics that underpin your system.
   b) Explain how your system adheres to or challenges current understanding of quantum biology.
   c) Discuss any potential limitations or challenges in implementing your system.

3. Information Theory Analysis (200-250 words):
   a) Analyze the information capacity of your quantum-genetic encoding system.
   b) Compare the information density of your system to classical DNA encoding.
   c) Discuss any implications for data compression or error correction in genetic information.

4. Implications for Genetic Engineering (250-300 words):
   a) Explore how your quantum-genetic encoding system could impact genetic engineering techniques.
   b) Propose a novel application of your system in genetic modification or synthetic biology.
   c) Discuss any ethical considerations related to the use of quantum states in genetic engineering.

5. Future Research Directions (150-200 words):
   a) Suggest three potential experiments to test or validate aspects of your quantum-genetic encoding system.
   b) Propose a research question that arises from your system design.
   c) Discuss how your system might contribute to our understanding of the relationship between quantum physics and biology.

Ensure your response demonstrates a deep understanding of quantum physics, genetics, and information theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings (a, b, c, d) within each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must propose a detailed system for encoding {t['genetic_element']['element']} using quantum states, specifically utilizing the property of {t['quantum_property']['property']}.",
            "The proposed system should demonstrate a clear understanding of both quantum physics and genetics, integrating concepts from both fields in a plausible manner.",
            "The submission must include all five required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation in the proposed quantum-genetic encoding system while maintaining scientific plausibility.",
            "The analysis of information theory aspects and implications for genetic engineering should be insightful and well-reasoned.",
            "The response must show a deep understanding of quantum physics, genetics, and information theory, using appropriate terminology from all fields.",
            "The proposed future research directions and experiments should be relevant and potentially feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

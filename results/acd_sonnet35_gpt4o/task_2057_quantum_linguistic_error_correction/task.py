import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                "concept": "Superposition",
                "description": "The ability of a quantum system to exist in multiple states simultaneously"
            },
            {
                "concept": "Entanglement",
                "description": "A quantum phenomenon where particles become correlated in such a way that the quantum state of each particle cannot be described independently"
            }
        ]
        return {
            "1": random.choice(quantum_concepts),
            "2": random.choice(quantum_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired language model for error correction in communication systems, focusing on the quantum concept of {t['concept']} ({t['description']}). Your task has the following components:\n\n1. Quantum-Linguistic Framework (250-300 words):\n   a) Explain how the concept of {t['concept']} can be applied to linguistic structures.\n   b) Describe how this quantum-inspired approach could enhance error correction in communication.\n   c) Propose a novel representation of linguistic units (e.g., words, phonemes) using quantum-inspired states.\n\n2. Error Correction Mechanism (200-250 words):\n   a) Detail the process of identifying and correcting errors using your quantum-inspired model.\n   b) Explain how your approach differs from classical error correction methods.\n   c) Provide a simple example demonstrating the error correction process.\n\n3. Mathematical Formulation (200-250 words):\n   a) Present the key mathematical equations or formalisms underlying your model.\n   b) Explain how these equations incorporate both quantum and linguistic principles.\n   c) Discuss any novel mathematical constructs you've developed for this purpose.\n\n4. Visual Representation (Include a text-based diagram or ASCII art):\n   Provide a visual representation of your quantum-inspired language model, illustrating key components and their interactions.\n\n5. Potential Applications (150-200 words):\n   a) Propose two potential applications of your quantum-inspired language model beyond error correction.\n   b) Explain how these applications could benefit from the unique properties of your approach.\n\n6. Implementation Challenges (150-200 words):\n   a) Discuss the main challenges in implementing your model in real-world communication systems.\n   b) Propose potential solutions or areas for further research to address these challenges.\n\n7. Comparative Analysis (200-250 words):\n   a) Compare your quantum-inspired model to traditional error correction methods in linguistics.\n   b) Analyze the potential advantages and limitations of your approach.\n   c) Discuss how your model might be integrated with existing communication technologies.\n\nEnsure your response demonstrates a deep understanding of quantum physics, information theory, and linguistics. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Quantum-Linguistic Framework:') on a new line, followed by your response for that section.\n\nYour total response should be between 1150-1450 words, not including the headings and the visual representation in section 4."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the quantum concept of {t['concept']} and its potential applications in linguistics and error correction.",
            "The proposed quantum-inspired language model is innovative yet grounded in scientific principles.",
            "The mathematical formulation is coherent and integrates quantum and linguistic concepts effectively.",
            "The visual representation clearly illustrates the key components and interactions of the quantum-inspired language model.",
            "The response includes a thoughtful analysis of potential applications and implementation challenges.",
            "The comparative analysis demonstrates a clear understanding of both quantum-inspired and traditional approaches to error correction.",
            "The response adheres to the specified format, including all required sections and word count limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

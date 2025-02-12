import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_linguistic_concepts = [
            {
                "concept": "Semantic Superposition",
                "description": "Words exist in a superposition of meanings until observed in context",
                "quantum_principle": "Quantum Superposition"
            },
            {
                "concept": "Entangled Translation",
                "description": "Pairs of words in different languages are entangled, affecting each other's translations instantly",
                "quantum_principle": "Quantum Entanglement"
            }
        ]
        return {
            "1": random.choice(quantum_linguistic_concepts),
            "2": random.choice(quantum_linguistic_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum-inspired language processing system based on the concept of {t['concept']}. Your task has four parts:\n\nBackground:\nQuantum superposition refers to the ability of quantum systems to exist in multiple states simultaneously until measured.\nQuantum entanglement is a phenomenon where two particles become interconnected, and the state of one instantly affects the other, regardless of distance.\n\n1. Concept Explanation (100-150 words):\n   a) Explain the quantum linguistic concept of {t['concept']}.\n   b) Describe how it relates to the quantum mechanical principle of {t['quantum_principle']}.\n   c) Discuss how this concept differs from classical approaches to language processing.\n\n2. System Design (200-250 words):\n   a) Describe the key components of your quantum linguistic system.\n   b) Explain how your system implements the {t['concept']} in its language processing.\n   c) Provide a high-level algorithm or process flow for your system.\n\n3. Application Example (150-200 words):\n   a) Present a specific example of how your system would process or translate a given text.\n   b) Explain step-by-step how the quantum linguistic principles are applied.\n   c) Compare the output or effectiveness of your system to a classical approach.\n\n4. Implications and Limitations (100-150 words):\n   a) Discuss potential advantages of your quantum linguistic system over classical methods.\n   b) Identify possible limitations or challenges in implementing this system.\n   c) Suggest potential applications or areas of research that could benefit from this approach.\n\nEnsure your response demonstrates a deep understanding of both quantum mechanics and linguistic principles. Be creative in your approach while maintaining scientific plausibility and logical consistency.\n\nPlease format your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the quantum linguistic concept of {t['concept']} and its relation to {t['quantum_principle']}.",
            "The system design is innovative, logically consistent, and effectively incorporates quantum principles into language processing.",
            "The application example clearly demonstrates how the quantum linguistic system would function in practice.",
            "The discussion of implications and limitations shows a nuanced understanding of both quantum mechanics and linguistics.",
            "The proposed system demonstrates creativity and novelty in applying quantum principles to linguistics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

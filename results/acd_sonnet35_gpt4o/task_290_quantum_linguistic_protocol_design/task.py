import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "wave-particle duality"
        ]
        linguistic_features = [
            "phonology",
            "morphology",
            "syntax",
            "semantics"
        ]
        tasks = {
            "1": {
                "quantum_property": random.choice(quantum_properties),
                "linguistic_feature": random.choice(linguistic_features)
            },
            "2": {
                "quantum_property": random.choice(quantum_properties),
                "linguistic_feature": random.choice(linguistic_features)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum communication protocol that utilizes the quantum property of {t['quantum_property']} and incorporates the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. Protocol Design (200-250 words):
   a) Explain how your protocol uses the given quantum property for communication.
   b) Describe how the specified linguistic feature is integrated into the protocol.
   c) Outline the basic steps or components of your quantum linguistic protocol.

2. Quantum-Linguistic Integration (150-200 words):
   a) Analyze how the quantum property and linguistic feature interact in your protocol.
   b) Discuss any novel emergent properties or capabilities that arise from this integration.

3. Information Encoding and Transmission (150-200 words):
   a) Explain how information is encoded in your quantum linguistic system.
   b) Describe the process of transmitting and receiving messages using your protocol.

4. Cognitive Implications (150-200 words):
   a) Speculate on how using this quantum linguistic protocol might affect human cognition or language processing.
   b) Discuss potential changes in thinking patterns or linguistic structures that could emerge.

5. Practical Applications and Limitations (150-200 words):
   a) Propose two potential real-world applications for your quantum linguistic protocol.
   b) Identify and explain at least two significant limitations or challenges of your protocol.

6. Ethical Considerations (100-150 words):
   Discuss potential ethical implications or concerns related to the development and use of your quantum linguistic protocol.

Ensure your response is creative, scientifically grounded, and demonstrates a deep understanding of both quantum mechanics and linguistics. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of the quantum property of {t['quantum_property']} and the linguistic feature of {t['linguistic_feature']}.",
            "The quantum linguistic protocol design should be creative, coherent, and scientifically plausible.",
            "The response should thoroughly address all six required sections, providing insightful analysis and speculation where appropriate.",
            "The integration of quantum mechanics and linguistics should be novel and well-reasoned.",
            "The response should demonstrate an interdisciplinary approach, effectively combining concepts from quantum physics, linguistics, and information theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principles": ["superposition", "entanglement"],
                "linguistic_features": ["phonemes", "morphemes"],
                "cultural_context": "Ancient Greek mythology",
                "message_to_encode": "Prometheus stole fire from the gods"
            },
            "2": {
                "quantum_principles": ["quantum tunneling", "wave function collapse"],
                "linguistic_features": ["syntax", "semantics"],
                "cultural_context": "Mayan calendar system",
                "message_to_encode": "The Long Count cycle ends and begins anew"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired linguistic encryption system and use it to encode and decode a culturally significant message. Your task has the following parts:

1. Encryption System Design (250-300 words):
   a) Create an encryption system that combines the quantum principles of {' and '.join(t['quantum_principles'])} with the linguistic features of {' and '.join(t['linguistic_features'])}.
   b) Explain how your system incorporates these quantum principles and linguistic features.
   c) Describe the encryption and decryption processes in detail.
   d) Discuss how your system maintains information security while preserving linguistic properties.

2. Cultural Integration (150-200 words):
   a) Explain how your encryption system incorporates elements from the cultural context of {t['cultural_context']}.
   b) Discuss how this cultural integration enhances the security or functionality of your system.

3. Message Encoding (200-250 words):
   a) Encode the following message using your quantum-linguistic encryption system: "{t['message_to_encode']}"
   b) Provide a step-by-step explanation of the encoding process.
   c) Discuss how the encoded message reflects both quantum and linguistic properties.

4. Decoding Demonstration (150-200 words):
   a) Demonstrate how the encoded message would be decrypted.
   b) Explain any challenges that might arise during decryption and how they are addressed.

5. Potential Applications (200-250 words):
   a) Propose two innovative applications for your quantum-linguistic encryption system outside of traditional cryptography.
   b) Explain how these applications could benefit from the unique properties of your system.
   c) Discuss any ethical considerations related to these applications.

6. Comparative Analysis (150-200 words):
   a) Compare your quantum-linguistic encryption system to traditional encryption methods.
   b) Discuss one advantage and one limitation of your system.
   c) Speculate on how quantum computing advancements might impact the effectiveness of your system in the future.

Ensure your response demonstrates a deep understanding of quantum mechanics principles, linguistic features, and the specified cultural context. Be creative in your approach while maintaining scientific and linguistic plausibility. Your total response should not exceed 2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of the encryption system that incorporates the specified quantum principles and linguistic features.",
            "The cultural context is meaningfully integrated into the encryption system design.",
            "The given message is encoded using the designed system, with a clear explanation of the process.",
            "The decoding process is demonstrated and explained.",
            "Two innovative applications for the encryption system are proposed and discussed.",
            "The response includes a comparative analysis with traditional encryption methods."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

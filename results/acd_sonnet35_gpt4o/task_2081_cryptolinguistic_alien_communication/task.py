import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "scenario": "First Contact",
                "cryptographic_principle": "Substitution Cipher",
                "linguistic_feature": "Tonal Language",
                "message_type": "Warning of Impending Supernova"
            },
            {
                "scenario": "Ancient Alien Artifact",
                "cryptographic_principle": "Diffie-Hellman Key Exchange",
                "linguistic_feature": "Logographic Writing System",
                "message_type": "Interstellar Coordinates"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and decoding fictional alien languages based on cryptographic principles, then use it to solve the following interstellar communication problem:

Scenario: {t['scenario']}
Cryptographic Principle to Incorporate: {t['cryptographic_principle']}
Linguistic Feature to Include: {t['linguistic_feature']}
Type of Message to Encode/Decode: {t['message_type']}

Your response should include the following sections:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for creating and decoding alien languages.
   b) Explain how your system incorporates the specified cryptographic principle and linguistic feature.
   c) Detail the mechanisms used for generating and analyzing novel symbolic systems.
   d) Discuss how your system balances linguistic plausibility with effective encryption.

2. Alien Language Design (200-250 words):
   a) Present a brief overview of the alien language created by your AI system.
   b) Explain how the language incorporates the specified linguistic feature.
   c) Describe how the cryptographic principle is applied in the language structure.
   d) Provide a small sample of the language (5-10 symbols or words) with their meanings.

3. Encoding/Decoding Process (200-250 words):
   a) Describe the step-by-step process your AI system uses to encode the specified message type.
   b) Explain the decoding procedure, including any key exchange or decryption steps.
   c) Discuss how your system handles potential ambiguities or contextual nuances in the message.

4. Interstellar Communication Solution (200-250 words):
   a) Present your solution to the given scenario using the designed alien language.
   b) Explain how the message is encoded and how it would be transmitted.
   c) Describe any additional metadata or context your system would provide to aid in decoding.
   d) Discuss potential challenges in real-world application of your solution.

5. Ethical and Practical Implications (150-200 words):
   a) Discuss the potential implications of AI-generated languages for SETI and interstellar communication.
   b) Address any ethical concerns related to the use of cryptographic alien languages.
   c) Explore the potential applications of your AI system beyond fictional scenarios.

Ensure your response demonstrates a deep understanding of linguistics, cryptography, and artificial intelligence. Be creative in your language design while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cryptography, and artificial intelligence.",
            "The AI system architecture is well-designed and incorporates the specified cryptographic principle and linguistic feature.",
            "The alien language design is creative, plausible, and effectively incorporates the required elements.",
            "The encoding/decoding process is clearly explained and logically sound.",
            "The interstellar communication solution effectively addresses the given scenario.",
            "The response discusses ethical and practical implications thoughtfully.",
            "The overall response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

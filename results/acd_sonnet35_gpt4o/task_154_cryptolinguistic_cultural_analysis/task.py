import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Zephyrians",
                "environment": "floating sky islands",
                "values": ["harmony with wind currents", "cloud shepherding", "aerial navigation"]
            },
            {
                "name": "Luminians",
                "environment": "bioluminescent underground caverns",
                "values": ["light cultivation", "echolocation", "mineral symbiosis"]
            }
        ]
        return {
            "1": random.choice(cultures),
            "2": random.choice(cultures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cryptographic writing system for the {t['name']} culture, who live in an environment of {t['environment']}. Then, use this system to encode and decode culturally significant messages. Your task has four parts:

1. Cryptographic System Design (200-250 words):
   a) Create a unique writing system that reflects the {t['name']} culture and their environment.
   b) Describe the basic elements (alphabet, syllabary, or logograms) and any special characters or modifiers.
   c) Explain how the system incorporates at least one cryptographic technique (e.g., substitution, transposition, steganography).
   d) Provide a brief example of how a simple word or phrase would be written and encrypted in this system.

2. Cultural Analysis (150-200 words):
   a) Explain how your cryptographic system reflects the values and environment of the {t['name']} culture.
   b) Describe how this writing system might influence the culture's social structures, education, or technological development.
   c) Discuss any taboos or sacred elements in the writing system and their cultural significance.

3. Message Encoding (100-150 words):
   a) Encode the following message using your cryptographic system: "{random.choice(t['values'])}"
   b) Explain the encoding process step by step.
   c) Describe any cultural connotations or hidden meanings in the encoded message.

4. Message Decoding (100-150 words):
   a) Provide a short encoded message (different from the one in part 3) in your cryptographic system.
   b) Explain the decoding process step by step.
   c) Reveal the decoded message and its cultural significance to the {t['name']}.

Ensure your response demonstrates a deep understanding of linguistic principles, cryptography, and cultural anthropology. Be creative in your design while maintaining internal consistency and cultural relevance."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed and creative design for a cryptographic writing system that reflects the given culture and environment.",
            "The cultural analysis demonstrates a nuanced understanding of how the writing system would influence and be influenced by the culture.",
            "The encoding and decoding processes are clearly explained and consistent with the described cryptographic system.",
            "The encoded and decoded messages are culturally relevant and demonstrate proper use of the cryptographic system.",
            "The overall response shows a strong grasp of linguistic principles, cryptography, and cultural anthropology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

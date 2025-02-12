import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "Confirmation bias",
            "Anchoring bias",
            "Availability heuristic",
            "Dunning-Kruger effect"
        ]
        linguistic_features = [
            "Phonological similarity",
            "Syntactic ambiguity",
            "Semantic priming",
            "Morphological derivation"
        ]
        return {
            "1": {"bias": random.choice(cognitive_biases), "feature": random.choice(linguistic_features)},
            "2": {"bias": random.choice(cognitive_biases), "feature": random.choice(linguistic_features)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cryptographic system based on the cognitive bias of {t['bias']} and the linguistic feature of {t['feature']}. Then, analyze its security and potential applications in cognitive enhancement. Your response should include:

1. Cryptographic System Design (250-300 words):
   a) Explain how your cryptographic system incorporates the given cognitive bias and linguistic feature.
   b) Describe the encryption and decryption processes, including any key generation methods.
   c) Provide an example of how a simple message would be encrypted and decrypted using your system.

2. Security Analysis (200-250 words):
   a) Analyze the strengths and weaknesses of your cryptographic system.
   b) Discuss potential vulnerabilities and attack vectors.
   c) Compare its security to a well-known traditional cryptographic method.

3. Cognitive Implications (200-250 words):
   a) Explain how using this cryptographic system might affect cognition or decision-making processes.
   b) Discuss potential cognitive biases that might be reinforced or mitigated through regular use of this system.
   c) Propose a hypothesis about how this system could be used for cognitive enhancement.

4. Practical Applications (150-200 words):
   a) Suggest two potential real-world applications for your cryptographic system.
   b) Explain how the cognitive and linguistic aspects of your system provide unique advantages in these applications.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using a cryptographic system based on cognitive biases and linguistic features.
   b) Address concerns related to privacy, manipulation, and cognitive influence.

Ensure your response demonstrates a deep understanding of cryptography, cognitive psychology, and linguistics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cryptographic system incorporates both {t['bias']} and {t['feature']} in its design",
            "The response includes a detailed description of the encryption and decryption processes",
            "The security analysis covers strengths, weaknesses, and potential vulnerabilities",
            "The cognitive implications are thoroughly discussed, including a hypothesis for cognitive enhancement",
            "Practical applications and ethical considerations are addressed",
            "The overall response demonstrates creativity, interdisciplinary knowledge, and analytical reasoning"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

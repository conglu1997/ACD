import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biochemical_processes = [
            "DNA replication",
            "protein folding",
            "enzyme catalysis",
            "signal transduction",
            "membrane transport"
        ]
        cryptographic_concepts = [
            "public key encryption",
            "digital signatures",
            "hash functions",
            "key exchange protocols",
            "zero-knowledge proofs"
        ]
        return {
            "1": {
                "biochemical_process": random.choice(biochemical_processes),
                "cryptographic_concept": random.choice(cryptographic_concepts)
            },
            "2": {
                "biochemical_process": random.choice(biochemical_processes),
                "cryptographic_concept": random.choice(cryptographic_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical cryptographic system based on the biochemical process of {t['biochemical_process']}, incorporating the cryptographic concept of {t['cryptographic_concept']}. Your response should include the following sections:

1. Biochemical-Cryptographic System Design (250-300 words):
   a) Describe the key components and mechanisms of your cryptosystem, explaining how it leverages the specified biochemical process.
   b) Explain how you incorporate the given cryptographic concept into your biochemical system.
   c) Provide a high-level diagram or flowchart of your system using ASCII art.

2. Encryption and Decryption Process (200-250 words):
   a) Explain the step-by-step process of encrypting a message using your biochemical cryptosystem.
   b) Describe the decryption process and how it relates to the biochemical mechanisms involved.
   c) Discuss any unique features or advantages of your system compared to traditional cryptographic methods.

3. Security Analysis (200-250 words):
   a) Analyze the potential strengths and vulnerabilities of your biochemical cryptosystem.
   b) Compare its security features to those of conventional cryptographic systems.
   c) Propose methods to enhance the security of your system or address potential weaknesses.

4. Practical Implementation Challenges (150-200 words):
   a) Identify the main challenges in implementing your theoretical system in a real-world context.
   b) Discuss any technological or biological limitations that need to be overcome.
   c) Propose potential solutions or areas of research to address these challenges.

5. Applications and Implications (200-250 words):
   a) Suggest two potential applications of your biochemical cryptosystem in fields such as medicine, data storage, or secure communications.
   b) Discuss the ethical implications of using biological processes for cryptographic purposes.
   c) Explore how your system might impact the future of cryptography and information security.

Ensure your response demonstrates a deep understanding of both biochemical processes and cryptographic principles. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biochemical_process']} and how it can be leveraged for cryptographic purposes.",
            f"The cryptographic system effectively incorporates the concept of {t['cryptographic_concept']}.",
            "The design is innovative yet scientifically plausible, showing a strong grasp of both biochemistry and cryptography principles.",
            "The response addresses all required sections with appropriate depth and insight.",
            "The security analysis and practical implementation challenges are thoughtfully discussed.",
            "The response includes an ASCII art diagram or flowchart illustrating the system design.",
            "The total word count is between 1000-1250 words, with each section adhering to its specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

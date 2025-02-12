import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = ['confirmation bias', 'anchoring bias', 'availability heuristic', 'framing effect', 'Dunning-Kruger effect']
        linguistic_patterns = ['metaphor', 'metonymy', 'synecdoche', 'hyperbole', 'litotes']
        encryption_types = ['substitution', 'transposition', 'steganography', 'one-time pad', 'public-key']
        
        return {
            "1": {
                "cognitive_bias": random.choice(cognitive_biases),
                "linguistic_pattern": random.choice(linguistic_patterns),
                "encryption_type": random.choice(encryption_types)
            },
            "2": {
                "cognitive_bias": random.choice(cognitive_biases),
                "linguistic_pattern": random.choice(linguistic_patterns),
                "encryption_type": random.choice(encryption_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel encryption system that incorporates the cognitive bias of {t['cognitive_bias']}, the linguistic pattern of {t['linguistic_pattern']}, and elements of {t['encryption_type']} encryption. Your response should include:

1. System Design (250-300 words):
   a) Describe the overall structure and functioning of your encryption system.
   b) Explain how it incorporates {t['cognitive_bias']} and {t['linguistic_pattern']}.
   c) Detail how elements of {t['encryption_type']} encryption are integrated.
   d) Provide a step-by-step example of how a simple message would be encrypted.

2. Cognitive Science Analysis (200-250 words):
   a) Explain how {t['cognitive_bias']} influences the encryption or decryption process.
   b) Discuss potential advantages or vulnerabilities this cognitive element introduces.
   c) Analyze how this system might interact with other cognitive biases or heuristics.

3. Linguistic Implications (200-250 words):
   a) Describe how {t['linguistic_pattern']} is utilized in your encryption system.
   b) Explain how this linguistic element affects the structure or interpretation of encrypted messages.
   c) Discuss any language-specific considerations or limitations of your system.

4. Cryptographic Strength (150-200 words):
   a) Analyze the theoretical strength of your encryption system.
   b) Compare its potential effectiveness to traditional {t['encryption_type']} methods.
   c) Identify potential vulnerabilities and propose ways to address them.

5. Ethical and Practical Considerations (150-200 words):
   a) Discuss potential ethical implications of an encryption system based on cognitive biases.
   b) Explore practical applications of your system in fields like cybersecurity or cognitive psychology.
   c) Propose guidelines for responsible development and use of cognitive-based encryption.

Ensure your response demonstrates a deep understanding of cryptography, cognitive science, and linguistics. Be innovative in your approach while maintaining scientific and mathematical plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The encryption system clearly incorporates {t['cognitive_bias']}, {t['linguistic_pattern']}, and elements of {t['encryption_type']} encryption.",
            "The system design is innovative yet scientifically plausible.",
            "The response demonstrates a deep understanding of cryptography, cognitive science, and linguistics.",
            "The analysis of cognitive and linguistic implications is thorough and insightful.",
            "The cryptographic strength of the system is critically analyzed.",
            "Ethical and practical considerations are thoughtfully explored.",
            "The response addresses all required sections with appropriate detail and length.",
            "The total response is between 950-1200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

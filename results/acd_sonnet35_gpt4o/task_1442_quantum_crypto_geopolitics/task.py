import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "crypto_algorithm": "Lattice-based cryptography",
                "geopolitical_context": "US-China technology competition",
                "specific_challenge": "Securing satellite communications"
            },
            {
                "crypto_algorithm": "Hash-based cryptography",
                "geopolitical_context": "European Union data sovereignty",
                "specific_challenge": "Cross-border financial transactions"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a post-quantum cryptography system based on {t['crypto_algorithm']} and analyze its geopolitical implications in the context of {t['geopolitical_context']}, with a focus on {t['specific_challenge']}. Your response should include the following sections:

1. Cryptographic System Design (300-350 words):
   a) Describe the key components and functioning of your post-quantum cryptography system.
   b) Explain how your system addresses potential vulnerabilities to quantum attacks.
   c) Discuss any trade-offs or limitations in your design.
   d) Provide a high-level pseudocode or diagram illustrating a key aspect of your system.

2. Technical Analysis (250-300 words):
   a) Compare your system's security and efficiency to current cryptographic standards.
   b) Analyze potential attack vectors and how your system mitigates them.
   c) Discuss the scalability and practical implementation challenges of your system.

3. Geopolitical Implications (250-300 words):
   a) Analyze how your cryptography system might affect the balance of power in {t['geopolitical_context']}.
   b) Discuss potential international cooperation or conflict arising from the development and deployment of your system.
   c) Consider how your system might influence national cybersecurity strategies and policies.

4. Specific Challenge Application (200-250 words):
   a) Explain how your cryptography system addresses {t['specific_challenge']}.
   b) Discuss any unique considerations or adaptations needed for this application.
   c) Analyze potential economic or strategic impacts of implementing your system in this context.

5. Ethical and Social Considerations (200-250 words):
   a) Discuss ethical implications of deploying your post-quantum cryptography system.
   b) Analyze potential social impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of post-quantum cryptography technologies.

6. Future Scenarios (150-200 words):
   a) Describe two potential future scenarios resulting from the widespread adoption of your cryptography system.
   b) Discuss how these scenarios might reshape international relations and cybersecurity landscapes.

Ensure your response demonstrates a deep understanding of quantum computing, cryptography, and international relations. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all six required sections, addressing {t['crypto_algorithm']}, {t['geopolitical_context']}, and {t['specific_challenge']}.",
            "The cryptographic system design demonstrates a clear understanding of post-quantum cryptography principles and potential quantum attacks.",
            "The geopolitical analysis shows a nuanced understanding of international relations and cybersecurity implications.",
            "The response addresses ethical considerations and proposes thoughtful guidelines for responsible development and use.",
            "The submission demonstrates creativity and innovation while maintaining scientific and technological plausibility.",
            "The response effectively integrates knowledge from quantum computing, cryptography, and international relations.",
            "The submission follows the required formatting with clear headings for each section and numbered paragraphs."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

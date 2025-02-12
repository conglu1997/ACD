import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_mechanisms = [
            "DNA replication",
            "Photosynthesis",
            "Neural signaling",
            "Immune system recognition",
            "Bacterial quorum sensing"
        ]
        
        information_challenges = [
            "Data compression",
            "Error correction",
            "Pattern recognition",
            "Distributed consensus",
            "Adaptive learning"
        ]
        
        return {
            "1": {
                "mechanism": random.choice(biological_mechanisms),
                "challenge": random.choice(information_challenges)
            },
            "2": {
                "mechanism": random.choice(biological_mechanisms),
                "challenge": random.choice(information_challenges)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired information processing system based on the biological mechanism of {t['mechanism']}, then apply it to solve the complex information processing challenge of {t['challenge']}. Your response should include the following sections:

1. Biological Mechanism Analysis (250-300 words):
   a) Explain the key features and processes of {t['mechanism']}.
   b) Discuss how this mechanism processes or transmits information in biological systems.
   c) Identify specific aspects that could be translated into an artificial information processing system.

2. Bio-inspired System Design (300-350 words):
   a) Describe the architecture of your bio-inspired information processing system.
   b) Explain how it mimics or adapts the principles of {t['mechanism']}.
   c) Discuss any novel features or improvements your system offers over traditional approaches.
   d) Include a high-level diagram or pseudocode of your system (describe it textually).

3. Application to {t['challenge']} (250-300 words):
   a) Explain how your bio-inspired system addresses the challenge of {t['challenge']}.
   b) Describe the specific algorithms or processes involved in solving this challenge.
   c) Discuss potential advantages of your approach compared to conventional methods.
   d) Provide a detailed case study or example scenario demonstrating your system's effectiveness.

4. Information Theoretic Analysis (200-250 words):
   a) Analyze your system's performance using relevant information theory concepts (e.g., entropy, mutual information, channel capacity).
   b) Quantitatively compare the information processing efficiency of your system to biological and traditional artificial systems.
   c) Discuss any trade-offs or limitations in your bio-inspired approach.

5. Broader Implications and Future Directions (200-250 words):
   a) Explore potential applications of your bio-inspired system in other domains.
   b) Discuss how this approach might contribute to our understanding of biological information processing.
   c) Propose two potential extensions or modifications to enhance your system's capabilities.

Ensure your response demonstrates a deep understanding of biology, information theory, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts. Your response should strike a balance between established scientific principles and novel, speculative ideas.

Format your response with clear headings for each section, numbered as above. Use subheadings (a, b, c, d) within each section as appropriate. Your total response should be between 1200-1450 words. Include a brief note at the end stating the word count of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the specified biological mechanism and its information processing aspects, using accurate and relevant biological terminology.",
            "The bio-inspired system design effectively incorporates principles from the biological mechanism and applies them innovatively to information processing, with a clear explanation of the system's architecture.",
            "The application to the given information processing challenge is well-reasoned, demonstrates potential advantages over conventional methods, and includes a detailed, plausible case study or example scenario.",
            "The information theoretic analysis is sound, uses relevant concepts correctly, and provides quantitative insights into the system's performance compared to biological and traditional artificial systems.",
            "The discussion of broader implications and future directions is insightful, considers multiple perspectives, and proposes novel yet plausible extensions of the system.",
            "The overall response strikes a balance between established scientific principles and creative, speculative ideas while maintaining plausibility.",
            "The response follows the specified format with clear headings for each section and adheres to the word count requirement."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

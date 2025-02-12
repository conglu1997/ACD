import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Japanese', 'Maori', 'Inuit', 'Yoruba', 'Andean', 'Ancient Greek']
        cognitive_domains = ['time', 'emotions', 'family relationships', 'power structures', 'nature', 'death']
        return {
            "1": {
                "culture": random.choice(cultures),
                "cognitive_domain": random.choice(cognitive_domains)
            },
            "2": {
                "culture": random.choice(cultures),
                "cognitive_domain": random.choice(cognitive_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting culturally-specific metaphors for {t['culture']} culture in the cognitive domain of {t['cognitive_domain']}. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of cognitive linguistics relevant to metaphor generation and interpretation.
   b) Discuss how cultural background influences metaphorical thinking in the given cognitive domain.
   c) Describe how these principles can be integrated into an AI system.

2. AI System Architecture (300-350 words):
   a) Outline the overall architecture of your AI system.
   b) Explain how it incorporates cultural knowledge and cognitive linguistic principles.
   c) Describe the main components and their interactions.
   d) Discuss any novel algorithms or approaches used in your design.

3. Metaphor Generation Process (200-250 words):
   a) Explain how your system would generate culturally-appropriate metaphors.
   b) Provide an example of a generated metaphor for the given culture and cognitive domain.
   c) Analyze the cultural and cognitive elements reflected in the generated metaphor.

4. Metaphor Interpretation Process (200-250 words):
   a) Describe how your system would interpret metaphors from the given culture and cognitive domain.
   b) Provide an example of a culturally-specific metaphor and your system's interpretation.
   c) Explain how the system accounts for cultural context in its interpretation.

5. Evaluation and Limitations (150-200 words):
   a) Propose methods to evaluate the cultural accuracy and cognitive validity of the generated and interpreted metaphors.
   b) Discuss potential limitations of your system and areas for improvement.
   c) Address ethical considerations related to AI systems working with cultural knowledge.

6. Broader Implications (150-200 words):
   a) Discuss how this AI system could contribute to our understanding of cultural cognition and linguistic diversity.
   b) Explore potential applications in fields such as cross-cultural communication, education, or AI ethics.
   c) Speculate on future developments in AI systems for cultural and cognitive modeling.

Ensure your response demonstrates a deep understanding of cognitive linguistics, cultural anthropology, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics and its application to metaphor generation and interpretation.",
            f"The AI system design effectively incorporates cultural knowledge specific to {t['culture']} culture.",
            f"The proposed system convincingly addresses the cognitive domain of {t['cognitive_domain']}.",
            "The metaphor generation and interpretation processes are well-explained and culturally appropriate.",
            "The response includes innovative approaches while maintaining scientific plausibility.",
            "Ethical considerations and limitations of the system are adequately addressed.",
            "The broader implications and potential applications of the system are insightfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

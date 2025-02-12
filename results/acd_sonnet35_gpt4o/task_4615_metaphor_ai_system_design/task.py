import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphor_types = [
            {'type': 'Structural metaphor', 'example': 'Life is a journey'},
            {'type': 'Orientational metaphor', 'example': 'Happy is up, sad is down'},
            {'type': 'Ontological metaphor', 'example': 'Inflation is an entity'},
            {'type': 'Container metaphor', 'example': 'The mind is a container'}
        ]
        return {str(i+1): metaphor for i, metaphor in enumerate(random.sample(metaphor_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating metaphors based on conceptual blending theory, with a focus on {t['type']} (e.g., '{t['example']}'). Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor processing and generation.
   b) Explain how your system incorporates conceptual blending theory and other relevant cognitive models.
   c) Detail how the system represents and manipulates conceptual spaces and mappings.
   d) Discuss any novel approaches in your design for handling the complexity and creativity of metaphorical language.

2. Metaphor Understanding Module (250-300 words):
   a) Explain how your system identifies and interprets metaphors in natural language input.
   b) Describe the process of mapping between source and target domains.
   c) Discuss how your system handles context and ambiguity in metaphor interpretation.
   d) Provide an example of how your system would process and understand a {t['type']}.

3. Metaphor Generation Module (250-300 words):
   a) Describe the process by which your system generates novel metaphors.
   b) Explain how conceptual blending is implemented in the generation process.
   c) Discuss how your system ensures the generated metaphors are coherent and meaningful.
   d) Provide an example of how your system would generate a new {t['type']}.

4. Evaluation and Testing (200-250 words):
   a) Propose methods for evaluating the performance of your metaphor AI system.
   b) Describe experiments to test both the understanding and generation capabilities.
   c) Discuss how you would measure the creativity and appropriateness of generated metaphors.
   d) Address potential challenges in evaluating metaphor processing systems.

5. Applications and Implications (200-250 words):
   a) Discuss potential applications of your metaphor AI system in fields such as natural language processing, creative writing, or cognitive science.
   b) Explore how this technology could enhance human-AI interaction or contribute to our understanding of human cognition.
   c) Address any ethical considerations related to AI systems that can understand and generate metaphorical language.

6. Limitations and Future Work (150-200 words):
   a) Identify current limitations of your proposed system.
   b) Discuss challenges in scaling the system to handle a wide range of metaphor types and domains.
   c) Suggest areas for future research and development in AI metaphor processing.

Ensure your response demonstrates a deep understanding of conceptual blending theory, metaphor in cognitive linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual blending theory, metaphor in cognitive linguistics, and artificial intelligence.",
            "The AI system design is innovative yet scientifically plausible.",
            "The system effectively incorporates conceptual blending theory and other relevant cognitive models.",
            "The response addresses all required sections with appropriate depth and clarity.",
            f"The proposed system adequately handles the specified metaphor type ({t['type']}) in both understanding and generation.",
            "The evaluation methods and potential applications are thoughtfully discussed.",
            "Limitations and future research directions are insightfully explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_modalities = [
            {
                "source": "visual",
                "target": "auditory",
                "concept": "complexity"
            },
            {
                "source": "tactile",
                "target": "olfactory",
                "concept": "intensity"
            }
        ]
        return {
            "1": random.choice(sensory_modalities),
            "2": random.choice(sensory_modalities)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating cross-modal metaphors, focusing on translating {t['concept']} from the {t['source']} modality to the {t['target']} modality. Then, analyze its implications for human cognition and AI development. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cross-modal metaphor generation and interpretation.
   b) Explain how your system processes and represents information from different sensory modalities.
   c) Detail the mechanisms for translating concepts between modalities, focusing on {t['concept']}.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Metaphor Generation (200-250 words):
   a) Explain the step-by-step process your system would use to generate a metaphor translating {t['concept']} from {t['source']} to {t['target']} modality.
   b) Provide an example of a generated metaphor and its explanation.
   c) Discuss any challenges in preserving the essence of {t['concept']} across modalities.

3. Cognitive Modeling (200-250 words):
   a) Describe how your system models human cognitive processes involved in cross-modal metaphor comprehension.
   b) Explain how your approach aligns with or challenges current theories in cognitive linguistics.
   c) Discuss potential insights your system might provide about human conceptual integration across senses.

4. Learning and Adaptation (150-200 words):
   a) Explain how your system could learn and improve its metaphor generation over time.
   b) Describe how it might adapt to different cultural or individual interpretations of sensory experiences.
   c) Propose a method for evaluating the quality and coherence of generated metaphors.

5. Implications for AI Development (200-250 words):
   a) Discuss how your system's approach to cross-modal metaphors could enhance general AI capabilities.
   b) Explain potential applications of your system in fields such as human-computer interaction, creative AI, or cognitive assistance.
   c) Describe how this technology might bridge the gap between symbolic and subsymbolic AI approaches.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues arising from the development or application of your AI system.
   b) Discuss how these issues might be addressed or mitigated.
   c) Consider the broader societal implications of AI systems capable of cross-modal conceptual integration.

7. Future Research Directions (100-150 words):
   a) Propose two novel research questions that arise from your system design.
   b) Suggest potential expansions or modifications to your system for future development.
   c) Discuss how your approach might contribute to our understanding of artificial general intelligence.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI principles. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of the AI system's architecture for cross-modal metaphor generation and interpretation, focusing on translating {t['concept']} from {t['source']} to {t['target']} modality",
            "The metaphor generation process is clearly explained with a novel and relevant example",
            "The cognitive modeling section demonstrates a deep understanding of human conceptual integration across senses",
            "The learning and adaptation section proposes plausible methods for improving and evaluating the system",
            "The implications for AI development are thoughtfully discussed with specific examples",
            "Ethical considerations are addressed with clear examples and potential solutions",
            "Future research directions are proposed with clear relevance to the field",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of linguistics, cognitive science, and AI concepts",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

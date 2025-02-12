import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "concept": "perseverance",
                "context": "business negotiation"
            },
            "2": {
                "source_culture": "Indian",
                "target_culture": "German",
                "concept": "success",
                "context": "academic achievement"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting culturally-specific metaphors and idioms, then apply it to a cross-cultural communication scenario. Your task has the following parts:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for generating and interpreting cultural metaphors and idioms.
   b) Explain how your system would incorporate cultural knowledge and linguistic patterns.
   c) Discuss any novel elements in your design that enable cross-cultural understanding.

2. Cultural Adaptation (150-200 words):
   a) Explain how your system would generate a metaphor or idiom for the concept of "{t['concept']}" in {t['source_culture']} culture.
   b) Describe how your system would then adapt this metaphor or idiom for {t['target_culture']} culture, maintaining the core meaning.
   c) Provide an example of the original and adapted metaphor/idiom.

3. Contextual Application (150-200 words):
   a) Describe how your AI system would apply the adapted metaphor/idiom in the context of {t['context']}.
   b) Explain how the system ensures the metaphor/idiom is appropriate and effective in this specific context.
   c) Discuss potential challenges in this application and how your system would address them.

4. Evaluation Methodology (100-150 words):
   a) Propose a method to evaluate the effectiveness and cultural appropriateness of your system's metaphor/idiom generation and adaptation.
   b) Describe metrics you would use to assess both linguistic creativity and cultural accuracy.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-cultural metaphor generation and interpretation.
   b) Propose safeguards or guidelines to ensure responsible use of such a system.

6. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Briefly describe how these extensions could enhance cross-cultural communication or understanding.

Ensure your response demonstrates a deep understanding of cultural anthropology, linguistics, and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive system architecture for generating and interpreting cultural metaphors and idioms",
            f"The system successfully generates and adapts a metaphor/idiom for '{t['concept']}' from {t['source_culture']} to {t['target_culture']} culture",
            f"The adapted metaphor/idiom is appropriately applied to the context of {t['context']}",
            "A clear evaluation methodology is proposed with relevant metrics",
            "Ethical considerations and safeguards are thoroughly discussed",
            "Two relevant future directions are suggested with clear explanations",
            "The response demonstrates deep understanding of cultural anthropology, linguistics, and AI systems",
            "The proposed system is creative while remaining scientifically and technologically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

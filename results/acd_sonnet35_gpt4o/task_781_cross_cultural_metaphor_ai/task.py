import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Zulu",
            "Inuit",
            "Mayan",
            "Arabic"
        ]
        cognitive_aspects = [
            "embodied cognition",
            "conceptual blending",
            "analogical reasoning",
            "mental imagery",
            "emotional processing"
        ]
        metaphors = [
            "Time is money",
            "Life is a journey",
            "Ideas are food",
            "Love is a battlefield",
            "Knowledge is light"
        ]
        return {
            "1": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "metaphor": random.choice(metaphors)
            },
            "2": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "cognitive_aspect": random.choice(cognitive_aspects),
                "metaphor": random.choice(metaphors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of modeling and simulating the cognitive processes involved in metaphor comprehension and generation across different cultures, focusing on translating metaphors from {t['source_culture']} culture to {t['target_culture']} culture. Your system should emphasize the role of {t['cognitive_aspect']} in metaphor processing. As a concrete example, consider how your system would handle the metaphor "{t['metaphor']}" in this cross-cultural context.

This task is particularly challenging due to the complex interplay between cognitive processes, linguistic structures, and cultural nuances involved in metaphor comprehension and generation. Your system must navigate these intricacies while maintaining cultural sensitivity and preserving the intended meanings of metaphors.

Your response should include the following sections, each with a clear heading:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for cross-cultural metaphor processing.
   b) Explain how your system incorporates {t['cognitive_aspect']} in its metaphor comprehension and generation processes.
   c) Detail how the system accounts for cultural differences between {t['source_culture']} and {t['target_culture']} cultures.
   d) Discuss any novel approaches or algorithms used in your design.

2. Knowledge Representation (200-250 words):
   a) Explain how cultural knowledge is represented and stored in your system.
   b) Describe how metaphorical concepts are encoded and linked to cultural contexts.
   c) Discuss how your system handles ambiguity and multiple interpretations of metaphors.

3. Metaphor Processing Workflow (250-300 words):
   a) Provide a step-by-step explanation of how your system processes the metaphor "{t['metaphor']}" from comprehension in the {t['source_culture']} culture to generation in the {t['target_culture']} culture.
   b) Highlight how {t['cognitive_aspect']} influences each stage of the process.
   c) Explain how your system ensures cultural appropriateness and preserves intended meanings.
   d) Provide a specific example of how the system would translate the given metaphor between the two cultures, including any necessary adaptations or alternative expressions.

4. Cross-Cultural Comparison (150-200 words):
   a) Compare and contrast how the metaphor "{t['metaphor']}" might be understood and used in {t['source_culture']} and {t['target_culture']} cultures.
   b) Discuss how your system accounts for these differences in its processing and translation.

5. Learning and Adaptation (150-200 words):
   a) Describe how your system learns and adapts to new metaphors and cultural contexts.
   b) Explain any mechanisms for handling novel or creative metaphors not previously encountered.
   c) Discuss how the system might evolve its understanding of {t['cognitive_aspect']} through experience.

6. Evaluation and Challenges (200-250 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system's metaphor translations.
   b) Discuss potential challenges or limitations in implementing your system, particularly regarding {t['cognitive_aspect']}.
   c) Suggest areas for future research or improvement in cross-cultural metaphor processing.

7. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to cross-cultural metaphor translation by AI.
   b) Discuss how your system addresses concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for the responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system must focus on translating metaphors from {t['source_culture']} culture to {t['target_culture']} culture.",
            f"The system design must emphasize the role of {t['cognitive_aspect']} in metaphor processing.",
            f"The response must include a specific example of processing and translating the metaphor \"{t['metaphor']}\" in the given cross-cultural context.",
            "The response must include a clear description of the system architecture, knowledge representation, and metaphor processing workflow.",
            "The response must include a comparison of how the given metaphor is understood and used in the source and target cultures.",
            "The explanation of learning and adaptation mechanisms must be provided.",
            "The response must include a discussion of evaluation methods, challenges, and ethical considerations.",
            "The response must demonstrate a deep understanding of cognitive science, linguistics, and artificial intelligence.",
            "The proposed system must be creative while maintaining scientific plausibility.",
            "The response must be formatted with clear headings for each section and adhere to the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

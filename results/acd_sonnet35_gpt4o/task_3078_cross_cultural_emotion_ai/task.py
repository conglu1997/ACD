import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']
        cultures = ['Japanese', 'Brazilian', 'Nigerian', 'Russian', 'Indian']
        contexts = ['professional', 'familial', 'romantic', 'conflict resolution']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'emotion': random.choice(emotions),
                'source_culture': random.choice(cultures),
                'target_culture': random.choice([c for c in cultures if c != tasks.get(str(i-1), {}).get('source_culture')]),
                'context': random.choice(contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding, translating, and generating emotionally nuanced language for the emotion of {t['emotion']} from {t['source_culture']} culture to {t['target_culture']} culture in a {t['context']} context. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain how your AI system understands and represents emotional nuances in language.
   b) Describe how it incorporates cultural knowledge specific to the source and target cultures.
   c) Discuss the role of context in emotional expression and interpretation across cultures.

2. System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system processes linguistic, emotional, and cultural input to generate appropriate output.
   c) Detail how your system incorporates theories from psychology, linguistics, and anthropology.
   d) Provide a visual representation of your system architecture (describe it textually).

3. Emotion Translation Process (250-300 words):
   a) Provide a step-by-step example of how your system would translate the emotional expression of {t['emotion']} from {t['source_culture']} to {t['target_culture']} culture in a {t['context']} context.
   b) Explain how this process ensures cultural sensitivity and emotional accuracy.
   c) Describe how your system handles potential mismatches or untranslatable concepts between cultures.

4. Evaluation Methods (200-250 words):
   a) Propose quantitative and qualitative methods to evaluate your system's ability to accurately translate emotional nuances across cultures.
   b) Describe how you would compare your system's output to human interpretations and translations.
   c) Suggest a novel metric for measuring the cross-cultural effectiveness of the generated emotional expressions.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss potential ethical issues related to AI-generated cross-cultural emotional translations.
   b) Address any limitations of your approach, particularly in capturing cultural and individual emotional variations.
   c) Propose guidelines for the responsible development and use of cross-cultural emotion AI systems.
   d) Suggest potential applications of your system beyond language translation.

Ensure your response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, linguistics, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, linguistics, and AI system design.",
            "The proposed AI system is innovative and scientifically plausible.",
            "The response addresses all required sections and subsections comprehensively.",
            "The conceptual framework effectively explains how the AI system understands and represents emotional nuances in language across cultures.",
            "The system architecture is well-described and incorporates relevant theories from psychology, linguistics, and anthropology.",
            "The emotion translation process is clearly explained with a specific example.",
            "The evaluation methods proposed are comprehensive and include a novel metric for cross-cultural effectiveness.",
            "Ethical considerations are thoroughly discussed, and guidelines for responsible development are proposed.",
            "The response uses appropriate terminology from all relevant fields and provides clear explanations for complex concepts.",
            "The total response is between 1200-1450 words and formatted correctly with clear headings and subsections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

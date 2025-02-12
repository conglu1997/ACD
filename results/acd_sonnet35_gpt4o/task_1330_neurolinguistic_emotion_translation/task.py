import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_pairs = [
            {
                "emotion": "Schadenfreude",
                "origin_culture": "German",
                "target_culture": "Japanese",
                "context": "A colleague's failed presentation"
            },
            {
                "emotion": "Saudade",
                "origin_culture": "Portuguese",
                "target_culture": "Korean",
                "context": "Reminiscing about a childhood home"
            },
            {
                "emotion": "Hygge",
                "origin_culture": "Danish",
                "target_culture": "Indian",
                "context": "A cozy evening with close friends"
            },
            {
                "emotion": "Ubuntu",
                "origin_culture": "African",
                "target_culture": "American",
                "context": "Community members helping a neighbor in need"
            }
        ]
        return {str(i+1): pair for i, pair in enumerate(random.sample(emotion_pairs, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate the emotional concept of "{t['emotion']}" from {t['origin_culture']} culture to {t['target_culture']} culture, based on neurolinguistic patterns and cultural context. Consider the following context: {t['context']}.

Your response should include the following sections:

1. Conceptual Framework (200-250 words):
   a) Explain the challenges in translating "{t['emotion']}" across cultures.
   b) Describe how neurolinguistic theories can inform your approach.
   c) Discuss how cultural context influences the expression and interpretation of "{t['emotion']}".

2. AI System Architecture (250-300 words):
   a) Design a detailed AI architecture for this emotion translation task.
   b) Explain each component of your architecture and its function.
   c) Describe how your system integrates neurolinguistic data with cultural knowledge.
   d) Include a diagram of your architecture (using ASCII art or a clear textual description).

3. Neurolinguistic Mapping (150-200 words):
   a) Explain how you will represent the neural correlates of "{t['emotion']}" in your system.
   b) Describe the linguistic features you will analyze to understand expressions of "{t['emotion']}".
   c) Discuss how your system accounts for cultural variations in processing "{t['emotion']}".

4. Translation Process (200-250 words):
   a) Outline the step-by-step process of translating "{t['emotion']}" in the given context.
   b) Provide a specific example of how your system would translate an expression of "{t['emotion']}" from {t['origin_culture']} to {t['target_culture']} culture in the context of {t['context']}.
   c) Explain how your system ensures cultural sensitivity and accuracy in the translation.

5. Evaluation Metrics (100-150 words):
   a) Propose three specific metrics to evaluate the performance of your emotion translation system.
   b) Explain how these metrics capture both neurolinguistic accuracy and cultural appropriateness.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-cultural emotion translation.
   b) Address issues such as cultural appropriation, misinterpretation, and the role of human expertise.

7. Future Research Directions (100-150 words):
   a) Identify two areas for future research to improve cross-cultural emotion translation.
   b) Suggest potential applications of this technology in fields such as psychology, anthropology, or international relations.

Ensure your response demonstrates a deep understanding of neurolinguistics, artificial intelligence, and cultural studies. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Begin each section with the heading (e.g., '1. Conceptual Framework:') followed by your response for that section. Your total response should be between 1100-1450 words, not including the architecture diagram."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neurolinguistics, AI, and cultural studies, specifically in relation to the emotion '{t['emotion']}'.",
            f"The AI system architecture is well-designed, clearly explained, and appropriate for translating '{t['emotion']}' across cultures.",
            f"The approach to emotion translation is innovative, scientifically grounded, and considers the specific context of {t['context']}.",
            f"The translation process and example are culturally sensitive, well-reasoned, and accurately reflect the nuances of both {t['origin_culture']} and {t['target_culture']} cultures.",
            f"Ethical considerations are thoughtfully addressed, particularly in relation to the challenges of translating '{t['emotion']}' across cultures.",
            "The response is well-structured, within the specified word count, and follows the required format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

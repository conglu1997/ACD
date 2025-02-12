import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        text_types = ['social media posts', 'literary prose', 'political speeches', 'personal letters']
        cognitive_theories = ['Appraisal Theory', 'Conceptual Act Theory', 'Somatic Marker Hypothesis']
        return {
            "1": {
                "emotion": random.choice(emotions),
                "text_type": random.choice(text_types),
                "cognitive_theory": random.choice(cognitive_theories)
            },
            "2": {
                "emotion": random.choice(emotions),
                "text_type": random.choice(text_types),
                "cognitive_theory": random.choice(cognitive_theories)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate text with specific emotional content based on cognitive linguistic theories of emotion. Your system should focus on the emotion of {t['emotion']}, primarily working with {t['text_type']}, and incorporate principles from the {t['cognitive_theory']} of emotion. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system, including its main components and their interactions.
   b) Explain how your system incorporates principles from the specified cognitive theory of emotion.
   c) Detail any novel algorithms or techniques your system employs for emotion recognition and generation in text.
   d) Discuss how your system handles the nuances and contextual nature of emotional expression in language.

2. Linguistic Analysis (250-300 words):
   a) Explain how your system analyzes text to identify emotional content, focusing on the specified emotion.
   b) Describe the linguistic features (e.g., lexical, syntactic, semantic) your system considers in its analysis.
   c) Discuss how your system accounts for cultural and contextual variations in emotional expression.
   d) Provide an example of how your system would analyze a short text (2-3 sentences) from the specified text type. Include the sample text and a detailed breakdown of the analysis process.

3. Emotion Generation (250-300 words):
   a) Detail how your system generates text with the specified emotional content.
   b) Explain the process of selecting appropriate words, phrases, and syntactic structures to convey the desired emotion.
   c) Describe how your system ensures coherence and naturalness in the generated text.
   d) Provide a short example (2-3 sentences) of text your system might generate for the specified text type and emotion. Explain the rationale behind the generated text.

4. Cognitive Model Integration (200-250 words):
   a) Explain how your system's emotion analysis and generation align with the specified cognitive theory of emotion.
   b) Discuss any challenges in translating theoretical concepts into computational models.
   c) Describe how your system might contribute to or challenge current understanding of the cognitive theory.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of an AI system that can analyze and generate emotionally charged text.
   b) Address concerns related to privacy, manipulation, and the potential for misuse.
   c) Propose guidelines for responsible development and use of emotion-aware AI systems.

6. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the accuracy and effectiveness of your system in emotion analysis and generation.
   b) Describe how you would validate your system's performance against human judgments of emotional content.
   c) Discuss the challenges in assessing the 'authenticity' of AI-generated emotional text.
   d) Suggest approaches for continually improving and updating your system.

Ensure your response demonstrates a deep understanding of cognitive linguistics, emotion theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['cognitive_theory']} and how it relates to emotional expression in language.",
            f"The system design effectively addresses the analysis and generation of text expressing {t['emotion']} in the context of {t['text_type']}.",
            "The proposed AI system integrates cognitive linguistics, emotion theory, and artificial intelligence in a novel and plausible manner.",
            "The response includes appropriate technical terminology and clear explanations for complex concepts.",
            "The ethical considerations and evaluation methods are thoughtfully addressed.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The provided examples for text analysis and generation are relevant, detailed, and demonstrate the system's capabilities effectively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

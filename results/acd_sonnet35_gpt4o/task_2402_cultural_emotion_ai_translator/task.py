import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Brazilian",
            "Ethiopian",
            "Finnish"
        ]
        emotions = [
            "Nostalgia",
            "Schadenfreude",
            "Wabi-sabi",
            "Saudade"
        ]
        modalities = [
            "Text",
            "Speech",
            "Facial expressions",
            "Body language"
        ]
        content_types = [
            "Poetry",
            "Short story",
            "Song lyrics",
            "Public speech"
        ]
        tasks = {
            "1": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "emotion": random.choice(emotions),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities),
                "content_type": random.choice(content_types)
            },
            "2": {
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "emotion": random.choice(emotions),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities),
                "content_type": random.choice(content_types)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate emotional expressions across different cultures, languages, and modalities, focusing on the following parameters:

Source Culture: {t['source_culture']}
Target Culture: {t['target_culture']}
Emotion: {t['emotion']}
Source Modality: {t['source_modality']}
Target Modality: {t['target_modality']}
Content Type: {t['content_type']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for cross-cultural emotion translation.
   b) Explain how your system incorporates cultural context, emotional nuances, and modality-specific features.
   c) Detail how the system handles the transition between the specified source and target cultures and modalities.
   d) Discuss any novel approaches or mechanisms in your design.

2. Emotional-Linguistic Mapping (250-300 words):
   a) Explain how your system maps the specified emotion between the source and target cultures.
   b) Provide examples of how this emotion might be expressed differently in each culture.
   c) Discuss challenges in representing and translating this emotion across the given modalities.

3. Content Analysis and Reinterpretation (300-350 words):
   a) Describe how your AI system would analyze a piece of {t['content_type']} expressing {t['emotion']} in the {t['source_culture']} culture and {t['source_modality']}.
   b) Explain the process of reinterpreting this content for the {t['target_culture']} culture in the {t['target_modality']}.
   c) Provide a brief example of the original content and its reinterpreted version (100-150 words each).

4. Evaluation and Validation (200-250 words):
   a) Propose a method to evaluate the accuracy and cultural appropriateness of your system's translations.
   b) Discuss potential biases in your model and how they might be mitigated.
   c) Suggest an experiment to validate your AI system's performance with human participants from both cultures.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss ethical implications of using AI for cross-cultural emotional translation.
   b) Address potential misuse or misinterpretation of the technology.
   c) Identify limitations of your approach and propose future research directions.

Ensure your response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of emotional intelligence, cross-cultural communication, and artificial intelligence",
            "The system architecture is well-designed and effectively incorporates cultural context, emotional nuances, and modality-specific features",
            "The emotional-linguistic mapping is thoughtful and provides insightful examples of cross-cultural differences",
            "The content analysis and reinterpretation process is clearly explained and the provided examples are creative and culturally appropriate",
            "The proposed evaluation method and experiment are well-designed and address potential biases",
            "Ethical considerations are thoroughly discussed and limitations are honestly addressed",
            "The response is innovative while maintaining scientific plausibility",
            "The writing is clear, well-structured, and uses appropriate technical terminology",
            "The response stays within the specified word limit and follows the required format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

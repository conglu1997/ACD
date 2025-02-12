import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        metaphors = [
            {
                "source_language": "English",
                "source_metaphor": "Time is money",
                "target_language": "Japanese",
                "cultural_context": "Japanese work culture"
            },
            {
                "source_language": "Mandarin Chinese",
                "source_metaphor": "生活是一场戏 (Life is a play/drama)",
                "target_language": "Spanish",
                "cultural_context": "Latin American magical realism"
            },
            {
                "source_language": "Arabic",
                "source_metaphor": "العلم نور (Knowledge is light)",
                "target_language": "Swahili",
                "cultural_context": "East African oral traditions"
            },
            {
                "source_language": "Russian",
                "source_metaphor": "Жизнь прожить — не поле перейти (Living life is not like crossing a field)",
                "target_language": "Hindi",
                "cultural_context": "Indian philosophy of karma and rebirth"
            }
        ]
        return {
            "1": random.choice(metaphors),
            "2": random.choice(metaphors)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze, translate, and generate metaphors across different languages and cultures. Your task involves the following steps:

1. Metaphor Analysis (150-200 words):
   a) Explain the meaning and cultural significance of the metaphor "{t['source_metaphor']}" in {t['source_language']}.
   b) Identify the source and target domains of the metaphor.
   c) Discuss any cultural-specific elements that might affect its interpretation.

2. Cross-Cultural Translation (200-250 words):
   a) Translate the metaphor into {t['target_language']}, considering the cultural context of {t['cultural_context']}.
   b) Explain your translation choices and any adaptations you made to preserve the metaphor's essence.
   c) Discuss challenges in maintaining both the literal and figurative meanings across languages.

3. Cognitive Analysis (150-200 words):
   a) Analyze how the metaphor might be processed cognitively in both source and target languages.
   b) Discuss any differences in conceptual mappings between the two cultures.
   c) Explain how these differences might affect comprehension and usage of the metaphor.

4. Novel Metaphor Generation (200-250 words):
   a) Create a new metaphor in {t['target_language']} that conveys a similar meaning to the original, but is more culturally relevant to {t['cultural_context']}.
   b) Explain the conceptual mappings in your new metaphor.
   c) Discuss how your metaphor reflects the target culture's values or worldview.

5. Computational Linguistics Perspective (150-200 words):
   a) Propose a method for automatically detecting and translating metaphors between languages.
   b) Discuss challenges in implementing such a system and potential solutions.
   c) Explain how this system could be evaluated for accuracy and cultural sensitivity.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining cultural sensitivity and scientific accuracy.

Format your response with clear headings for each section. Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of metaphor analysis and cross-cultural translation.",
            "The cognitive analysis shows insight into how metaphors are processed in different languages and cultures.",
            "The newly generated metaphor is creative, culturally relevant, and effectively conveys a similar meaning to the original.",
            "The computational linguistics perspective provides a plausible method for automatic metaphor detection and translation.",
            "The overall response shows a high level of linguistic knowledge, cultural sensitivity, and creative thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

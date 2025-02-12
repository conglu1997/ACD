import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        idioms = [
            {
                "source_language": "English",
                "target_language": "Japanese",
                "idiom": "It's raining cats and dogs",
                "context": "describing heavy rainfall"
            },
            {
                "source_language": "Spanish",
                "target_language": "Russian",
                "idiom": "Estar como pez en el agua",
                "context": "feeling completely comfortable or at ease in a situation"
            },
            {
                "source_language": "French",
                "target_language": "Mandarin Chinese",
                "idiom": "Avoir le cafard",
                "context": "feeling down or depressed"
            },
            {
                "source_language": "German",
                "target_language": "Arabic",
                "idiom": "Ich verstehe nur Bahnhof",
                "context": "not understanding anything"
            }
        ]
        return {str(i+1): idiom for i, idiom in enumerate(random.sample(idioms, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the {t['source_language']} idiomatic expression "{t['idiom']}" into {t['target_language']}, preserving its cultural nuances and emotional impact. The idiom is used in the context of {t['context']}.

Your response should include:

1. Direct Translation (30-50 words):
   Provide a word-for-word translation of the original idiom into the target language.

2. Equivalent Idiom (30-50 words):
   Suggest an equivalent idiomatic expression in the target language that conveys a similar meaning and emotional impact.

3. Cultural Analysis (100-150 words):
   Explain the cultural significance of both the original and translated idioms. Discuss any differences in connotation, usage, or cultural context.

4. Emotional Impact (50-75 words):
   Compare the emotional impact of the original and translated idioms. Consider factors such as intensity, tone, and associated imagery.

5. Usage Example (50-75 words):
   Provide an example sentence or dialogue in the target language using the translated idiom, along with its English translation.

6. Translation Challenges (50-75 words):
   Discuss any specific linguistic or cultural challenges encountered during the translation process and how you addressed them.

Ensure your translation and analysis demonstrate a deep understanding of both languages and cultures involved. Be creative in finding equivalent expressions while maintaining the essence of the original idiom."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate detail.",
            "The translation preserves the cultural nuances and emotional impact of the original idiom.",
            "The cultural analysis demonstrates a deep understanding of both source and target cultures.",
            "The equivalent idiom in the target language is appropriate and conveys a similar meaning.",
            "The usage example correctly incorporates the translated idiom in context.",
            "The response explicitly addresses linguistic or cultural challenges encountered during the translation process."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "Japanese",
                "target_language": "English",
                "poetic_form": "Haiku",
                "theme": "Nature"
            },
            {
                "source_language": "Spanish",
                "target_language": "Mandarin Chinese",
                "poetic_form": "Sonnet",
                "theme": "Love"
            },
            {
                "source_language": "Arabic",
                "target_language": "Russian",
                "poetic_form": "Free Verse",
                "theme": "Urban Life"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for automated poetry translation from {t['source_language']} to {t['target_language']}, focusing on the {t['poetic_form']} form and the theme of {t['theme']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the main components of your translation system.
   b) Explain how your system processes and analyzes the source poem.
   c) Detail the translation process, including how semantic meaning and stylistic elements are preserved.
   d) Discuss any novel algorithms or techniques used in your system.

2. Linguistic and Poetic Analysis (250-300 words):
   a) Explain how your system handles the specific linguistic features of {t['source_language']} and {t['target_language']}.
   b) Describe how your system preserves the characteristics of the {t['poetic_form']} form.
   c) Discuss how your system maintains the theme of {t['theme']} across languages.

3. Cultural Adaptation (200-250 words):
   a) Explain how your system accounts for cultural differences in poetic expression.
   b) Describe any techniques used to preserve culturally specific imagery or metaphors.
   c) Discuss how your system handles cases where direct translation might lose cultural significance.

4. Example Translation (200-250 words):
   a) Provide a short example poem in the source language ({t['source_language']}).
   b) Show your system's translation of this poem into the target language ({t['target_language']}).
   c) Analyze how your system preserved meaning, form, and style in this example.

5. Evaluation Metrics (150-200 words):
   a) Propose metrics to evaluate the quality of your system's translations.
   b) Explain how these metrics account for both semantic accuracy and poetic quality.
   c) Describe how you would validate your system's performance.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of automated poetry translation.
   b) Address issues related to authorship and creativity in machine-translated poetry.
   c) Identify limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of linguistics, poetry, and machine translation. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and cultural plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address all six sections specified in the instructions",
            f"The system design should be tailored for translating {t['poetic_form']} on the theme of {t['theme']} from {t['source_language']} to {t['target_language']}",
            "The response should demonstrate a deep understanding of linguistics, poetry, and machine translation",
            "The proposed system should be innovative while maintaining scientific and cultural plausibility",
            "The example translation should be provided and analyzed effectively",
            "The response should address ethical considerations and limitations of automated poetry translation"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

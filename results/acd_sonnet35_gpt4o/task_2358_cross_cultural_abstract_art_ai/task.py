import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Japanese',
                'historical_period': 'Edo period',
                'emotion': 'Wabi-sabi (imperfect beauty)'
            },
            {
                'culture': 'African',
                'historical_period': 'Contemporary',
                'emotion': 'Ubuntu (interconnectedness)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of interpreting and generating abstract art across different cultures and historical periods, then apply it to analyze and create artwork based on the emotion of {t['emotion']} in {t['culture']} culture during the {t['historical_period']}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for interpreting and generating abstract art.
   b) Explain how it processes visual information and maps it to cultural and emotional concepts.
   c) Detail how the system accounts for cultural and historical context in its interpretation and generation processes.
   d) Include a high-level diagram or pseudocode representing the system's workflow.

2. Cultural and Historical Context Module (200-250 words):
   a) Explain how your system incorporates knowledge of {t['culture']} culture and the {t['historical_period']}.
   b) Describe any specific algorithms or models used for cultural and historical context understanding.
   c) Discuss how the system handles variations in artistic styles and techniques within this cultural and historical framework.

3. Emotion-to-Abstract Art Mapping (200-250 words):
   a) Describe how your system maps the emotion of {t['emotion']} to visual elements in abstract art.
   b) Explain any techniques used to ensure cultural sensitivity and accuracy in emotional representation.
   c) Provide a brief example of how the system might interpret an existing abstract artwork expressing {t['emotion']} from the specified culture and period.

4. Abstract Art Generation (250-300 words):
   a) Explain the process by which your AI system would generate an original abstract artwork expressing {t['emotion']} in the style of {t['culture']} art from the {t['historical_period']}.
   b) Describe the key visual elements, techniques, or symbols the system might employ.
   c) Discuss how the system ensures the generated art is both culturally appropriate and emotionally evocative.
   d) Provide a textual description of the abstract artwork your system would generate.

5. Ethical and Cultural Sensitivity Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI for cross-cultural art interpretation and generation.
   b) Address concerns related to cultural appropriation, misrepresentation, or potential misuse.
   c) Propose guidelines for responsible development and use of such systems in the art world.

6. Evaluation and Future Improvements (150-200 words):
   a) Suggest methods to evaluate the effectiveness and cultural accuracy of your system's art interpretation and generation.
   b) Propose two potential improvements or expansions to enhance its capabilities in cross-cultural abstract art understanding.
   c) Discuss any limitations of your current design and how they might be addressed in future iterations.

Ensure your response demonstrates a deep understanding of art history, cultural studies, emotions, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Format your response using clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['culture']} culture and art from the {t['historical_period']}.",
            f"The AI system effectively maps the emotion of {t['emotion']} to visual elements in abstract art.",
            "The abstract art generation process is well-explained and culturally appropriate.",
            "The response addresses ethical considerations and cultural sensitivity.",
            "The evaluation methods and future improvements are thoughtfully considered."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

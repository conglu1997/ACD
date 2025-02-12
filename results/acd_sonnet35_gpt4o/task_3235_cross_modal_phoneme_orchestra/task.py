import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Xhosa', 'Finnish', 'Mandarin', 'Arabic', 'Inuktitut']
        musical_styles = ['Baroque', 'Jazz', 'Minimalist', 'Romantic', 'Avant-garde']
        phonetic_features = ['place of articulation', 'manner of articulation', 'voicing']
        musical_elements = ['pitch', 'rhythm', 'timbre', 'dynamics']
        
        return {
            "1": {
                "language": random.choice(languages),
                "musical_style": random.choice(musical_styles),
                "phonetic_feature": random.choice(phonetic_features),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "language": random.choice(languages),
                "musical_style": random.choice(musical_styles),
                "phonetic_feature": random.choice(phonetic_features),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates phonemes into musical elements based on cross-modal perception principles, then use it to create a musical composition from a given text in {t['language']}. Your system should focus on the phonetic feature of {t['phonetic_feature']}, primarily utilize the musical element of {t['musical_element']}, and compose in the style of {t['musical_style']} music. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your cross-modal phoneme-to-music translation system.
   b) Explain how you map the chosen phonetic feature to the specified musical element.
   c) Detail how you incorporate principles of cross-modal perception and synesthesia into your translation process.
   d) Discuss any novel algorithms or techniques used in your design.

2. Linguistic Analysis (200-250 words):
   a) Explain how your system analyzes and processes the phonetic feature of {t['phonetic_feature']} in {t['language']}.
   b) Describe any challenges specific to this language and how your system addresses them.
   c) Discuss how your system handles phonemes that may not exist in more familiar languages.

3. Musical Composition Process (250-300 words):
   a) Provide a step-by-step explanation of how your system generates music from the analyzed phonemes.
   b) Describe how you ensure the composed music adheres to the principles of {t['musical_style']} music.
   c) Explain how the {t['musical_element']} is manipulated to reflect the phonetic input.

4. Cross-modal Mapping (200-250 words):
   a) Detail how your system implements the mapping between {t['phonetic_feature']} and {t['musical_element']}.
   b) Explain any research or theories you've incorporated to support this cross-modal mapping.
   c) Discuss potential challenges or limitations in representing phonetic features through music.

5. Sample Composition (150-200 words):
   a) Provide a short text input in {t['language']} (2-3 sentences) and describe the musical composition your system would generate from it.
   b) Explain how the composition reflects the input text, chosen phonetic feature, musical element, and musical style.

6. Evaluation and Implications (150-200 words):
   a) Propose methods to evaluate the effectiveness and artistic merit of your system's compositions.
   b) Discuss potential applications of your system in fields such as linguistics, music therapy, or language learning.
   c) Consider ethical implications of using AI to create cross-modal art based on unfamiliar languages.

Ensure your response demonstrates a deep understanding of linguistics, music theory, and cross-modal perception. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, music theory, and cross-modal perception.",
            f"The system design effectively maps the phonetic feature of {t['phonetic_feature']} to the musical element of {t['musical_element']}.",
            f"The linguistic analysis shows a good understanding of {t['language']} and its phonetic properties.",
            f"The musical composition process adheres to the principles of {t['musical_style']} music.",
            "The cross-modal mapping is well-explained and grounded in relevant research or theories.",
            "The sample composition description effectively illustrates how the system works.",
            "The evaluation methods and implications discussed are insightful and relevant.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

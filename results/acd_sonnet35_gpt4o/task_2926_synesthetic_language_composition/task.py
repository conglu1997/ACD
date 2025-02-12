import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "Phonemes",
            "Syntax",
            "Semantics",
            "Prosody"
        ]
        musical_elements = [
            "Pitch",
            "Rhythm",
            "Harmony",
            "Timbre"
        ]
        synesthetic_associations = [
            "Color-to-sound",
            "Shape-to-sound",
            "Texture-to-sound",
            "Emotion-to-sound"
        ]
        genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "World music"
        ]
        tasks = {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "musical_element": random.choice(musical_elements),
                "synesthetic_association": random.choice(synesthetic_associations),
                "genre": random.choice(genres)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "musical_element": random.choice(musical_elements),
                "synesthetic_association": random.choice(synesthetic_associations),
                "genre": random.choice(genres)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates language into music based on synesthetic principles, then use it to compose a musical piece from a given text. Your system should focus on the linguistic feature of {t['linguistic_feature']}, the musical element of {t['musical_element']}, and incorporate the synesthetic association of {t['synesthetic_association']}. The final composition should be in the style of {t['genre']} music.

Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your synesthetic language-to-music translation system.
   b) Explain how you map the chosen linguistic feature to the specified musical element.
   c) Detail how you incorporate the given synesthetic association into your translation process.
   d) Discuss any novel algorithms or techniques used in your design.

2. Linguistic Analysis (200-250 words):
   a) Explain how your system analyzes and processes the linguistic feature of {t['linguistic_feature']} in the input text.
   b) Describe any pre-processing steps or natural language processing techniques used.
   c) Discuss how your system handles variations or complexities in this linguistic feature.

3. Musical Composition Process (250-300 words):
   a) Provide a step-by-step explanation of how your system generates music from the analyzed text.
   b) Describe how you ensure the composed music adheres to the principles of {t['genre']} music.
   c) Explain how the {t['musical_element']} is manipulated to reflect the linguistic input and synesthetic association.

4. Synesthetic Mapping (200-250 words):
   a) Detail how your system implements the {t['synesthetic_association']} in the translation process.
   b) Explain any research or theories you've incorporated to support this synesthetic mapping.
   c) Discuss potential challenges or limitations in representing this synesthetic experience through music.

5. Sample Composition (150-200 words):
   a) Provide a short text input (2-3 sentences) and describe the musical composition your system would generate from it.
   b) Explain how the composition reflects the input text, chosen linguistic feature, musical element, and synesthetic association.

6. Evaluation and Implications (150-200 words):
   a) Propose methods to evaluate the effectiveness and artistic merit of your system's compositions.
   b) Discuss potential applications of your system in fields such as music therapy, language learning, or artistic expression.
   c) Consider ethical implications of using AI to create synesthetic art.

Ensure your response demonstrates a deep understanding of linguistics, music theory, and synesthesia. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive system design that integrates {t['linguistic_feature']}, {t['musical_element']}, and {t['synesthetic_association']}.",
            f"The linguistic analysis effectively explains how the system processes {t['linguistic_feature']}.",
            f"The musical composition process clearly describes how {t['musical_element']} is manipulated in the style of {t['genre']} music.",
            f"The synesthetic mapping for {t['synesthetic_association']} is well-explained and grounded in research or theory.",
            "The sample composition description effectively demonstrates the system's capabilities.",
            "The response demonstrates deep understanding and creative integration of linguistics, music theory, and synesthesia."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

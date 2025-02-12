import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Mexican",
            "Egyptian",
            "Indian",
            "Australian Aboriginal"
        ]
        art_elements = [
            "Color symbolism",
            "Geometric patterns",
            "Texture",
            "Negative space",
            "Balance and composition"
        ]
        emotions = [
            "Joy",
            "Sorrow",
            "Anger",
            "Serenity",
            "Anxiety"
        ]
        return {
            "1": {
                "culture": random.choice(cultures),
                "art_element": random.choice(art_elements),
                "emotion": random.choice(emotions)
            },
            "2": {
                "culture": random.choice(cultures),
                "art_element": random.choice(art_elements),
                "emotion": random.choice(emotions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of creating and interpreting abstract art across different cultural contexts, then use it to generate and analyze a piece of abstract art for the {t['culture']} culture. Your AI system should focus on the art element of {t['art_element']} and aim to evoke the emotion of {t['emotion']}. Provide your response in the following format:

1. AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system for creating and interpreting abstract art.
   b) Explain how your system incorporates cultural knowledge and artistic principles.
   c) Discuss how the system handles the chosen art element ({t['art_element']}) and emotion ({t['emotion']}).
   d) Outline any novel approaches or techniques used in your design.

2. Cultural Context Analysis (200-250 words):
   a) Provide a brief overview of the artistic traditions and cultural symbolism in {t['culture']} culture.
   b) Explain how your AI system would interpret and incorporate these cultural elements.
   c) Discuss any challenges in representing {t['culture']} cultural concepts in abstract art.

3. Art Generation Process (200-250 words):
   a) Describe step-by-step how your AI system would generate an abstract art piece for the given parameters.
   b) Explain how the system ensures cultural authenticity while maintaining artistic creativity.
   c) Discuss how the chosen art element ({t['art_element']}) is emphasized in the generation process.

4. Emotion Evocation (150-200 words):
   a) Explain how your AI system attempts to evoke the emotion of {t['emotion']} in the generated art.
   b) Discuss the challenges of translating emotions into visual elements across cultures.
   c) Describe any feedback mechanisms your system might use to gauge emotional impact.

5. Art Interpretation (200-250 words):
   a) Provide a detailed interpretation of the generated abstract art piece.
   b) Analyze how effectively it incorporates {t['culture']} cultural elements and {t['art_element']}.
   c) Evaluate how well the piece evokes the intended emotion of {t['emotion']}.
   d) Discuss any unexpected or emergent properties in the generated art.

6. Ethical and Cultural Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI to create culturally-specific art.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of such AI systems.

7. Future Improvements and Applications (100-150 words):
   a) Suggest potential enhancements to your AI system for better cultural understanding or artistic creativity.
   b) Propose two novel applications of your system beyond abstract art generation.

Ensure your response demonstrates a deep understanding of both AI technologies and artistic principles, as well as sensitivity to cultural nuances. Use appropriate terminology from relevant fields and provide clear explanations of complex concepts. Be creative in your approach while maintaining plausibility and cultural respect.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['culture']} culture and its artistic traditions",
            f"The AI system effectively incorporates and emphasizes the art element of {t['art_element']}",
            f"The generated abstract art piece convincingly evokes the emotion of {t['emotion']}",
            "The AI system design is innovative, plausible, and respectful of cultural nuances",
            "The response addresses ethical considerations and proposes responsible guidelines",
            "The interpretation of the generated art piece is insightful and culturally informed",
            "The response demonstrates interdisciplinary knowledge across AI, art, and cultural studies"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

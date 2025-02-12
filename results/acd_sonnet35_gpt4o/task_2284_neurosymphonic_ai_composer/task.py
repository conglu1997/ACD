import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            {
                "style": "Western Classical",
                "emotion": "Melancholy",
                "cultural_context": "19th century European romanticism"
            },
            {
                "style": "Indian Raga",
                "emotion": "Serenity",
                "cultural_context": "Traditional Hindustani classical music"
            },
            {
                "style": "West African Polyrhythm",
                "emotion": "Joy",
                "cultural_context": "Yoruba ceremonial music"
            },
            {
                "style": "Japanese Gagaku",
                "emotion": "Reverence",
                "cultural_context": "Imperial court music of Japan"
            },
            {
                "style": "Andean Folk",
                "emotion": "Nostalgia",
                "cultural_context": "Traditional music of the Andes mountains"
            }
        ]
        return {str(i+1): style for i, style in enumerate(random.sample(musical_styles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models human music cognition to compose emotionally evocative pieces in various cultural styles. Then, apply your system to compose a short piece in the {t['style']} style, evoking the emotion of {t['emotion']}, within the cultural context of {t['cultural_context']}.

Your response should include the following sections:

1. Neurocognitive Music Model (300-350 words):
   a) Describe the key components of your AI system that model human music cognition.
   b) Explain how your model integrates neurological processes, music theory, and cultural knowledge.
   c) Detail how your system processes and generates emotional content in music.
   d) Provide a diagram or flowchart of your system's architecture (describe it textually).

2. Cultural Adaptation Mechanism (250-300 words):
   a) Explain how your system adapts to different musical styles and cultural contexts.
   b) Describe the data sources and learning mechanisms used to acquire cultural musical knowledge.
   c) Discuss how your system balances universal musical principles with culture-specific elements.

3. Emotional Mapping (250-300 words):
   a) Detail how your system maps emotions to musical elements (e.g., rhythm, melody, harmony, timbre).
   b) Explain how cultural context influences these emotion-music mappings.
   c) Describe any challenges in modeling subjective emotional experiences in music.

4. Composition Process (300-350 words):
   a) Provide a step-by-step explanation of how your system would compose a piece in the given style and emotion.
   b) Describe specific musical elements and techniques your system would employ to evoke the required emotion.
   c) Explain how your system ensures cultural authenticity in the composition.

5. Output Analysis (200-250 words):
   a) Describe the expected characteristics of the composed piece.
   b) Analyze how the composition reflects both the intended emotion and cultural style.
   c) Discuss potential variations in human interpretation of the AI-generated piece.

6. Ethical and Artistic Implications (200-250 words):
   a) Discuss ethical considerations in developing AI systems that create culturally-specific art.
   b) Analyze the potential impact of AI composers on human musicians and musical traditions.
   c) Explore the philosophical question of creativity and authorship in AI-generated music.

7. Future Directions (150-200 words):
   a) Suggest two potential improvements or expansions to your system.
   b) Discuss how this technology might impact fields such as music therapy, cross-cultural communication, or music education.
   c) Propose a related challenge in music cognition or AI composition that could be addressed using a similar approach.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Use bullet points or numbered lists where appropriate to organize your ideas. Your total response should be between 1800-2200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a detailed AI system modeling human music cognition for composing in various cultural styles",
            f"The system must be specifically applied to compose a piece in the {t['style']} style, evoking {t['emotion']}, within the context of {t['cultural_context']}",
            "The response should demonstrate deep understanding of neuroscience, music theory, and artificial intelligence, using appropriate terminology",
            "The composition process should be explained in detail, showing how it integrates cognitive modeling, cultural knowledge, and emotional mapping",
            "The response must address ethical and artistic implications of AI-generated culturally-specific music",
            "The response should be well-structured with clear headings for each required section and use bullet points or numbered lists where appropriate",
            "The response should be creative and scientifically plausible, without relying on generic or vague statements",
            "The total response should be between 1800-2200 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

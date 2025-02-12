import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion": "melancholy",
                "musical_style": "classical",
                "language": "English",
                "color_scheme": "cool colors (blues, purples)",
                "musical_phrase": "A minor key, slow tempo, descending melody",
                "color_code": "#4B0082 (Indigo)",
                "linguistic_expression": "The weight of memories pressed upon my heart"
            },
            {
                "emotion": "exhilaration",
                "musical_style": "electronic dance music",
                "language": "Spanish",
                "color_scheme": "warm colors (reds, oranges, yellows)",
                "musical_phrase": "Upbeat tempo, major key, rising arpeggios",
                "color_code": "#FFA500 (Orange)",
                "linguistic_expression": "Mi corazón late con la energía del universo"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate emotional states between music, language, and color, then use it to compose a multi-modal emotional narrative. Focus on the emotion of {t['emotion']}, using the musical style of {t['musical_style']}, the {t['language']} language, and a {t['color_scheme']} color scheme. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for translating emotions across modalities.
   b) Explain how your system integrates music theory, linguistics, and color psychology.
   c) Detail the neural network architecture or other AI techniques used in your system.
   d) Discuss how your system handles the challenges of cross-modal emotional translation.
   e) Explain how your system incorporates principles from cognitive science, such as embodied cognition or conceptual metaphor theory.

2. Emotional Representation (200-250 words):
   a) Explain how your system represents the emotion of {t['emotion']} in each modality (music, language, color).
   b) Describe the features or parameters used to capture emotional content in each domain.
   c) Discuss how your system ensures consistency of emotional representation across modalities.
   d) Explain how your system would process the given musical phrase: "{t['musical_phrase']}"

3. Translation Process (200-250 words):
   a) Detail the step-by-step process of translating {t['emotion']} from music to language to color.
   b) Explain any intermediate representations or transformations used in the translation process.
   c) Describe how your system handles ambiguities or cultural differences in emotional expression.
   d) Demonstrate how your system would translate the given color code {t['color_code']} into musical and linguistic representations.

4. Multi-modal Narrative Composition (250-300 words):
   a) Outline the process of composing a multi-modal narrative expressing {t['emotion']}.
   b) Provide a brief example of the composed narrative, including:
      - A short musical phrase or description (in {t['musical_style']} style)
      - A sentence or phrase in {t['language']} (with English translation)
      - A description of the corresponding color composition
   c) Explain how the different modalities work together to enhance the emotional impact.
   d) Describe how your system would incorporate the given linguistic expression: "{t['linguistic_expression']}"

5. Evaluation and Challenges (150-200 words):
   a) Propose methods for evaluating the effectiveness of your system in conveying emotions.
   b) Discuss potential limitations or challenges specific to the chosen emotion and modalities.
   c) Suggest ideas for future improvements or expansions of the system.

6. Code Snippet (50-100 words of explanation + code):
   Provide a small Python code snippet (15-25 lines) that demonstrates a key aspect of your system, such as the emotional representation or cross-modal translation process. Briefly explain what the code does and how it relates to your overall system design.

Ensure your response demonstrates a deep understanding of music theory, linguistics, color psychology, cognitive science, and AI techniques. Be innovative in your approach while maintaining scientific and technological plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words, excluding the code snippet."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of translating {t['emotion']} across music, language, and color modalities.",
            "The proposed AI system architecture is innovative, coherent, and technologically plausible, incorporating relevant cognitive science principles.",
            f"The multi-modal narrative effectively conveys {t['emotion']} using {t['musical_style']}, {t['language']}, and {t['color_scheme']}.",
            "The explanation of the translation process is clear and demonstrates understanding of cross-modal integration.",
            "The response addresses challenges and limitations specific to emotional translation and multi-modal synthesis.",
            "The provided code snippet is relevant, well-explained, and demonstrates a key aspect of the system.",
            "The response effectively incorporates and processes the given musical phrase, color code, and linguistic expression.",
            "The overall response showcases interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

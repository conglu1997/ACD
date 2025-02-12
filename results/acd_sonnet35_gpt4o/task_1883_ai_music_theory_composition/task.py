import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "music_concept_1": "Polyrhythm",
                "music_concept_2": "Modal interchange",
                "composition_style_1": "Minimalism",
                "composition_style_2": "Jazz fusion",
                "emotional_theme": "Tension and release"
            },
            {
                "music_concept_1": "Serialism",
                "music_concept_2": "Microtonality",
                "composition_style_1": "Avant-garde",
                "composition_style_2": "Indian classical",
                "emotional_theme": "Transcendence and grounding"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing, interpreting, and composing music based on complex music theory concepts. Then, use this system to create, explain, and compare original compositions. Your task has the following components:

1. AI System Design (250-300 words):
   a) Describe the key components and architecture of your AI music composition system.
   b) Explain how your system incorporates and understands complex music theory concepts.
   c) Discuss how the system balances creativity with adherence to musical rules and structures.
   d) Explain how your system can adapt to different musical styles and traditions.

2. Music Theory Analysis (250-300 words):
   a) Explain the concepts of {t['music_concept_1']} and {t['music_concept_2']} in music theory.
   b) Describe how your AI system would analyze and interpret these concepts in existing musical pieces.
   c) Discuss how these concepts relate to the emotional impact of music.
   d) Compare and contrast how these concepts are typically used in {t['composition_style_1']} and {t['composition_style_2']}.

3. Composition Generation and Comparison (300-350 words):
   a) Use your AI system to generate two short musical compositions (describe them in words):
      - Composition 1: Incorporates {t['music_concept_1']} in the style of {t['composition_style_1']}
      - Composition 2: Incorporates {t['music_concept_2']} in the style of {t['composition_style_2']}
      Both compositions should convey the emotional theme of {t['emotional_theme']}
   b) Provide a detailed explanation of each composition, including:
      - How it incorporates the specified music theory concept
      - How it adheres to the chosen compositional style
      - How it conveys the given emotional theme
   c) Compare and contrast the two compositions, discussing how the different concepts and styles affect the emotional impact.
   Note: Provide vivid textual descriptions of the compositions, including details about melody, harmony, rhythm, and instrumentation.

4. Creative Variations (150-200 words):
   a) Describe how your AI system could generate variations of one of the compositions by incorporating elements of the other.
   b) Explain how these variations might affect the emotional impact of the piece.
   c) Discuss the challenges and opportunities in blending different musical concepts and styles.

5. Implications and Limitations (150-200 words):
   a) Discuss the potential implications of AI-generated music for human composers and the music industry.
   b) Address any limitations or challenges in your AI music composition system, particularly in handling diverse musical traditions.
   c) Suggest areas for future research or improvement in AI music composition and cross-cultural musical analysis.

Ensure your response demonstrates a deep understanding of music theory, AI systems, and creative composition across different musical traditions. Use appropriate musical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining musical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a comprehensive design for an AI system capable of analyzing and composing music based on complex music theory concepts across different musical traditions.",
            f"The response must thoroughly explain the concepts of {t['music_concept_1']} and {t['music_concept_2']}, and how they are used in {t['composition_style_1']} and {t['composition_style_2']}.",
            f"The response must describe two distinct compositions incorporating the specified concepts and styles, conveying the theme of {t['emotional_theme']}, and provide a detailed comparison between them.",
            "The response must discuss creative variations that blend different musical concepts and styles.",
            "The response must address implications, limitations, and future directions for AI in music composition and cross-cultural musical analysis.",
            "The response should demonstrate a deep understanding of music theory, AI systems, and creative composition across diverse musical traditions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

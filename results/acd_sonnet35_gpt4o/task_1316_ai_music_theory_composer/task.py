import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            {
                "style": "Baroque counterpoint",
                "key_features": "Use of counterpoint, intricate ornamentations, and basso continuo"
            },
            {
                "style": "Jazz fusion",
                "key_features": "Complex harmonies, irregular time signatures, and improvisation"
            }
        ]
        return {
            "1": random.choice(musical_styles),
            "2": random.choice(musical_styles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating music based on advanced music theory concepts, then use it to compose a piece in the style of {t['style']}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI music theory and composition system.
   b) Explain how it incorporates advanced music theory concepts (e.g., harmony, counterpoint, form).
   c) Detail the components for musical analysis, generation, and style emulation.
   d) Discuss how the system handles creative decision-making in composition.

2. Music Theory Integration (200-250 words):
   a) Explain how your AI system represents and processes key music theory concepts.
   b) Describe how it analyzes existing music to learn stylistic features.
   c) Discuss any novel approaches your system uses to understand musical structure.

3. Style-Specific Composition (250-300 words):
   a) Describe how your AI system would approach composing in the style of {t['style']}.
   b) Explain how it incorporates the key features: {t['key_features']}.
   c) Provide a detailed description (100-150 words) of a short musical piece (16-32 measures) that your AI would generate in this style.
   d) Include a simple musical notation or representation (described in words) of a key motif from your AI-generated composition.
   e) Discuss any challenges in emulating this particular style and how your system addresses them.

4. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the musical quality and stylistic accuracy of the AI-generated compositions.
   b) Describe how your AI system could improve its compositions based on feedback.
   c) Suggest a specific metric for measuring the system's creativity in music generation.

5. Cognitive and Perceptual Considerations (150-200 words):
   a) Discuss how your AI system might incorporate principles of music cognition or perception.
   b) Explain how this could enhance the emotional or aesthetic impact of the generated music.
   c) Address any potential limitations in AI-generated music compared to human composition.

6. Ethical and Cultural Implications (100-150 words):
   a) Discuss potential ethical considerations in using AI for music composition.
   b) Address the impact of AI-generated music on human composers and the music industry.
   c) Consider the cultural implications of AI systems emulating specific musical styles or traditions.

7. Broader Applications (100-150 words):
   a) Propose two potential applications of your AI music system beyond composition.
   b) Briefly explain how these applications could benefit or impact the music industry or related fields.

Ensure your response demonstrates a deep understanding of both music theory and AI systems design. Be creative and innovative while maintaining technical feasibility. Use appropriate musical and AI terminology throughout your answer.

Your total response should be between 1200-1550 words. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly explain an AI system capable of analyzing and generating music in the style of {t['style']}.",
            "The AI system design should demonstrate a clear and plausible integration of advanced music theory concepts and AI principles.",
            f"The composition description should reflect key features of {t['style']}: {t['key_features']}.",
            "The submission must include all seven required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation in AI music system design while maintaining technical feasibility.",
            "The analysis of cognitive, ethical, and cultural implications should be insightful and well-reasoned.",
            "The response must show a deep understanding of both music theory and AI systems design.",
            "The response should include a simple musical notation or representation of a key motif from the AI-generated composition.",
            "The broader applications section should propose realistic and innovative uses of the AI music system beyond composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0

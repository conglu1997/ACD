import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "visual_art": "A black square on a white background",
                "artist": "Kazimir Malevich",
                "target_medium": "music"
            },
            {
                "visual_art": "The Persistence of Memory (melting clocks in a surreal landscape)",
                "artist": "Salvador Dalí",
                "target_medium": "poetry"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following abstract visual artwork and translate it into a different artistic medium:

Visual Artwork: {t['visual_art']} by {t['artist']}
Target Medium: {t['target_medium']}

Your task is to:

1. Visual Analysis (200-250 words):
   a) Describe the key visual elements of the artwork.
   b) Analyze the composition, use of color, shapes, and space.
   c) Interpret the possible meanings or emotions conveyed by the visual elements.

2. Conceptual Interpretation (200-250 words):
   a) Identify the main themes or ideas expressed in the artwork.
   b) Explain how these themes relate to the artist's known style or philosophy.
   c) Discuss any historical or cultural context that informs your interpretation.

3. Cross-Modal Translation (250-300 words):
   Cross-modal translation involves expressing the essence of one art form in another medium.
   a) Translate the key elements and themes of the visual artwork into the specified target medium.
   b) Describe your translation conceptually, explaining how each element corresponds to the original.
   c) Justify your creative choices in the translation process.
   Note: Do not generate or describe actual images, music, or poetry. Focus on the conceptual translation.

4. Comparative Analysis (200-250 words):
   a) Compare and contrast the original visual artwork with your translated version.
   b) Analyze how the change in medium affects the expression of the core concepts.
   c) Discuss any new meanings or interpretations that emerge through the translation.

5. Reflection on Cross-Modal Creativity (150-200 words):
   a) Reflect on the challenges and insights gained from this cross-modal translation process.
   b) Discuss how this exercise relates to human cognition and creativity.
   c) Speculate on the implications for AI systems attempting similar tasks.

Ensure your response demonstrates a deep understanding of both visual art and the target medium, as well as the ability to draw meaningful connections between different forms of artistic expression. Be creative and insightful in your interpretation and translation while maintaining logical consistency in your analysis.

Format your response with clear headings for each section as numbered above. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a thorough visual analysis of the artwork, identifying key elements and their potential meanings.",
            "The conceptual interpretation demonstrates understanding of the artist's style and relevant historical/cultural context.",
            f"The cross-modal translation effectively captures the essence of the original artwork in the {t['target_medium']} medium, without generating actual images, music, or poetry.",
            "The comparative analysis insightfully discusses the similarities and differences between the original and translated works.",
            "The reflection on cross-modal creativity shows depth of thought about the cognitive processes involved.",
            "The response demonstrates creativity and originality in interpretation and translation.",
            "The analysis maintains logical consistency and coherence throughout.",
            "The response adheres to the specified format with clear headings and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
